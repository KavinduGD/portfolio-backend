import asyncHandler from "express-async-handler";
import fs from "fs/promises";
import path from "path";
import { Request, Response } from "express";
import Project from "../models/projectModel";
import Technology from "../models/technologyModel";

const getProjects = asyncHandler(async (req: Request, res: Response) => {
  const projects = await Project.find({});

  const projectsWithImageUrls = projects.map((project) => {
    return {
      projectID: project._id,
      projectImageUrls: project.projectImages.map(
        (projectImage) =>
          `${req.protocol}://${req.get("host")}/uploads/project/${projectImage}`,
      ),
      architectureImageUrls: project.architectureImages.map((archImage) => {
        return {
          diagramName: archImage.diagramName,
          link: `${req.protocol}://${req.get("host")}/uploads/project/${archImage.imageName}`,
        };
      }),
      projectName: project.projectName,
      projectDescription: project.projectDescription,
      startedDate: project.startedDate,
      technologies: project.technologies,
      links: project.links,
      architectureDescription: project.architectureDescription,
      tags: project.tags,
      score: project.score,
    };
  });

  res.status(200).json(projectsWithImageUrls);
});

const addProject = asyncHandler(async (req: Request, res: Response) => {
  const files = req.files as Express.Multer.File[];

  try {
    const {
      projectName,
      projectDescription,
      startedDate,
      technologies,
      links,
      architectureDescription,
      tags,
      score,
    } = req.body;

    if (
      !projectName ||
      !projectDescription ||
      !startedDate ||
      !technologies ||
      !architectureDescription ||
      !tags ||
      !score ||
      !links
    ) {
      res.status(400);
      throw new Error("All required fields must be provided");
    }

    if (!files || files.length === 0) {
      res.status(400);
      throw new Error("Images are required");
    }

    // project images
    const projectImages = files
      .filter((image) => image.fieldname === "project-image")
      .map((image) => image.filename);

    // must have 2 image
    if (projectImages.length !== 2) {
      res.status(400);
      throw new Error("2 Project images are required");
    }

    // architecture images

    const architectureImages: {
      diagramName: string;
      imageName: string;
    }[] = [];

    for (const file of files) {
      const match = file.fieldname.match(/architecture\[(\d+)\]\[image\]/);

      if (!match) continue;

      const index = match[1];

      const diagramName = req.body.architecture[index]?.diagramName;

      if (!diagramName) {
        res.status(400);
        throw new Error("Invalid Image names");
      }

      architectureImages.push({
        diagramName,
        imageName: file.filename,
      });
    }

    if (architectureImages.length < 1 || architectureImages.length > 4) {
      res.status(400);
      throw new Error("Number of architecture image are invalid");
    }

    const technologiesList = JSON.parse(technologies);

    for (const technology of technologiesList) {
      const t = await Technology.findById(technology);

      if (!t) {
        res.status(400);
        throw new Error("Invalid Technology ID");
      }
    }

    const project = await Project.create({
      projectName,
      projectDescription,
      startedDate,
      technologies: JSON.parse(technologies),
      projectImages,
      links: JSON.parse(links),
      architectureImages,
      architectureDescription,
      tags: JSON.parse(tags),
      score: Number(score),
    });

    res.json({
      message: "Project added successfully",
      project: {
        projectID: project._id,
        projectImageUrls: project.projectImages.map(
          (projectImage) =>
            `${req.protocol}://${req.get("host")}/uploads/project/${projectImage}`,
        ),
        architectureImageUrls: project.architectureImages.map((archImage) => {
          return {
            diagramName: archImage.diagramName,
            link: `${req.protocol}://${req.get("host")}/uploads/project/${archImage.imageName}`,
          };
        }),
        projectName: project.projectName,
        projectDescription: project.projectDescription,
        startedDate: project.startedDate,
        technologies: project.technologies,
        links: project.links,
        architectureDescription: project.architectureDescription,
        tags: project.tags,
        score: project.score,
      },
    });
  } catch (err) {
    try {
      for (const file of files) {
        const filePath = path.join(
          process.cwd(),
          "uploads",
          "project",
          file.filename,
        );
        await fs.unlink(filePath);
      }
    } catch (error) {
      res.status(500);
      throw new Error("Server Error");
    }
    // res.status(500);
    throw err;
  }
});

const updateProject = asyncHandler(async (req: Request, res: Response) => {
  res.json({ message: "Update a project" });
});

const deleteProject = asyncHandler(async (req: Request, res: Response) => {
  const { id } = req.params;

  const project = await Project.findById(id);

  if (!project) {
    res.status(404);
    throw new Error("Project not found");
  }

  await project.deleteOne();

  // delete project images
  for (const image of project.projectImages) {
    const imagePath = path.join(process.cwd(), "uploads", "project", image);
    await fs.unlink(imagePath);
  }

  //delete arch image
  for (const image of project.architectureImages) {
    const imagePath = path.join(
      process.cwd(),
      "uploads",
      "project",
      image.imageName,
    );
    await fs.unlink(imagePath);
  }
  res.status(200).json({
    message: "Project deleted successfully",
  });
});

export { getProjects, addProject, updateProject, deleteProject };
