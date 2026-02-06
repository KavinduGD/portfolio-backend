import { Request, Response } from "express";
import asyncHandler from "express-async-handler";
import Skill from "../models/skillModel";
import fs from "fs/promises";
import path from "path";

const getSkills = asyncHandler(async (req: Request, res: Response) => {
  const skills = await Skill.find({});

  const skillsWithImageUrls = skills.map((skill) => {
    return {
      skillID: skill._id,
      skill: skill.skill,
      description: skill.description,
      imageUrl: `${req.protocol}://${req.get("host")}/uploads/skill/${skill.skillImage}`,
    };
  });

  res.status(200).json(skillsWithImageUrls);
});

const addSkill = asyncHandler(async (req: Request, res: Response) => {
  if (!req.file) {
    res.status(400);
    throw new Error("Icon image is required");
  }

  const { skill, description } = req.body;

  if (!skill || !description) {
    await fs.unlink(req.file.path);
    res.status(400);
    throw new Error("All field are required");
  }

  const newSkill = new Skill({
    skill,
    description,
    skillImage: req.file.filename,
  });

  try {
    const savedNewSkill = await newSkill.save();

    res.status(201);
    res.json({
      message: "Skill added successfully",
      skill: {
        id: savedNewSkill._id,
        skill: savedNewSkill.skill,
        description: savedNewSkill.description,
        imageUrl: `${req.protocol}://${req.get("host")}/uploads/skill/${savedNewSkill.skillImage}`,
      },
    });
  } catch (err: any) {
    await fs.unlink(req.file.path);

    if (err.code === 11000) {
      res.status(409);
      throw new Error("Skill already exists");
    }

    res.status(500);
    throw err;
  }
});

const updateSkill = asyncHandler(async (req: Request, res: Response) => {
  const { id } = req.params;

  const skill = await Skill.findById(id);

  if (!skill) {
    res.status(404);
    throw new Error("Invalid Skill ID");
  }

  let updates = req.body;

  if (req.file) {
    updates.skillImage = req.file.filename;
  }

  try {
    const updatedSkill = await Skill.findByIdAndUpdate(
      id,
      { $set: updates },
      { new: true, runValidators: true },
    );

    // delete the old image is if update is successful
    try {
      if (req.file) {
        const existingImagePath = path.join(
          process.cwd(),
          "uploads",
          "skill",
          skill.skillImage,
        );

        await fs.unlink(existingImagePath);
      }
    } catch (err) {
      res.status(500);
      throw err;
    }

    res.status(200).json({
      message: "Skill updated successfully",
      skill: {
        id: updatedSkill!._id,
        skill: updatedSkill!.skill,
        description: updatedSkill!.description,
        imageUrl: `${req.protocol}://${req.get("host")}/uploads/skill/${updatedSkill!.skillImage}`,
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

const deleteSkill = asyncHandler(async (req: Request, res: Response) => {
  const { id } = req.params;

  const skill = await Skill.findById(id);

  if (!skill) {
    res.status(404);
    throw new Error("Skill not found");
  }

  await skill.deleteOne();

  const imagePath = path.join(
    process.cwd(),
    "uploads",
    "skill",
    skill.skillImage,
  );

  await fs.unlink(imagePath);

  res.status(200).json({
    message: "Skill deleted successfully",
  });
});

export { getSkills, addSkill, updateSkill, deleteSkill };
