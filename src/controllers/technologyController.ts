import { Request, Response } from "express";
import asyncHandler from "express-async-handler";
import fs from "fs/promises";
import Technology from "../models/technologyModel";
import path from "path";

const getAllTechnologies = asyncHandler(async (req: Request, res: Response) => {
  const technologies = await Technology.find({});

  const technologiesWithImageUrl = technologies.map((technology) => {
    return {
      id: technology._id,
      technology: technology.technology,
      level: technology.level,
      type: technology.type,
      imageUrl: `${req.protocol}://${req.get("host")}/uploads/technology/${technology.icon}`,
    };
  });
  res.status(200).json(technologiesWithImageUrl);
});

const addTechnology = asyncHandler(async (req: Request, res: Response) => {
  if (!req.file) {
    res.status(400);
    throw new Error("Icon image is required");
  }

  const { technology, level, type } = req.body;

  if (!technology || !level || !type) {
    await fs.unlink(req.file.path);
    res.status(400);
    throw new Error("All fields are required");
  }

  const newTechnology = new Technology({
    technology,
    level,
    type,
    icon: req.file.filename,
  });

  try {
    const savedNewTechnology = await newTechnology.save();

    res.status(201).json({
      message: "Technology added successfully",
      technology: {
        id: savedNewTechnology._id,
        technology: savedNewTechnology.technology,
        level: savedNewTechnology.level,
        type: savedNewTechnology.type,
        imageUrl: `${req.protocol}://${req.get("host")}/uploads/technology/${savedNewTechnology.icon}`,
      },
    });
  } catch (err: any) {
    await fs.unlink(req.file.path);

    if (err.code === 11000) {
      res.status(409);
      throw new Error("Technology already exists");
    }

    res.status(500);
    throw err;
  }
});

const updateTechnology = asyncHandler(async (req, res) => {
  // path params
  const { id } = req.params;

  const technology = await Technology.findById(id);

  if (!technology) {
    res.status(404);
    throw new Error("Invalid Technology ID");
  }

  // update fields
  let updates = req.body;

  if (req.file) {
    updates = { ...updates, icon: req.file!.filename };
  }

  try {
    const updatedTechnology = await Technology.findByIdAndUpdate(
      id,
      { $set: updates },
      { new: true, runValidators: true },
    );
    // delete the old is if update is successful

    try {
      if (req.file) {
        const existingImagePath = path.join(
          process.cwd(),
          "uploads",
          "technology",
          technology.icon,
        );

        await fs.unlink(existingImagePath);
      }
    } catch (err) {
      res.status(500);
      throw err;
    }

    res.status(200).json({
      message: "Technology Updated successfully",
      updatedTechnology: {
        id: updatedTechnology!._id,
        technology: updatedTechnology!.technology,
        level: updatedTechnology!.level,
        type: updatedTechnology!.type,
        imageUrl: `${req.protocol}://${req.get("host")}/uploads/technology/${updatedTechnology!.icon}`,
      },
    });
  } catch (err: any) {
    if (req.file) {
      await fs.unlink(req.file.path);
    }
    res.status(500);
    throw err;
  }
});

const deleteTechnology = asyncHandler(async (req, res) => {
  const { id } = req.params;

  const technology = await Technology.findById(id);

  if (!technology) {
    res.status(404);
    throw new Error("Technology not found");
  }

  await technology.deleteOne();

  const imagePath = path.join(
    process.cwd(),
    "uploads/technology",
    technology.icon,
  );

  await fs.unlink(imagePath);

  res.status(200).json({
    message: "Technology deleted successfully",
  });
});

export {
  addTechnology,
  getAllTechnologies,
  updateTechnology,
  deleteTechnology,
};
