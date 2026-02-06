import { Request, Response } from "express";
import asyncHandler from "express-async-handler";
import User from "../models/userModel";

const getUserData = asyncHandler(async (req: Request, res: Response) => {
  const user = await User.findOne();

  if (!user) {
    res.status(404);
    throw new Error("There are no user in the DB");
  }

  res.status(200).json(user);
});

const addUser = asyncHandler(async (req: Request, res: Response) => {
  const {
    fullName,
    shortname,
    email,

    about,
    age,
    address,
    languages,
    phone,
    jobTitle,
    education,
  } = req.body;

  if (
    !fullName ||
    !shortname ||
    !email ||
    !about ||
    !age ||
    !address ||
    !languages ||
    !phone ||
    !jobTitle ||
    !education
  ) {
    res.status(400);
    throw new Error("All fields are required");
  }

  const existingUser = await User.findOne();

  if (existingUser) {
    res.status(409);
    throw new Error("One user exists in the Database");
  }

  const newUser = new User({
    fullName,
    shortname,
    email,
    about,
    age,
    address,
    languages,
    phone,
    jobTitle,
    education,
  });

  const savedUser = await newUser.save();

  res.status(201).json({
    message: "User Added successfully",
    user: savedUser,
  });
});

const updateUser = asyncHandler(async (req: Request, res: Response) => {
  const updates = req.body;
  const user = await User.findOne();

  if (!user) {
    res.status(404);
    throw new Error("User do not exists");
  }

  // Mongoose uses strict: true by default
  // ✅ Result
  // Fields defined in the schema → updated
  // Fields NOT in the schema (like anotherFeild) → IGNORED

  const updatedUser = await User.findByIdAndUpdate(
    user._id,
    { $set: updates }, // Use $set to update only specific fields
    { new: true, runValidators: true }, // Return the updated document and run schema validators
  );

  res.status(200).json({
    message: "User updated successfully",
    user: updatedUser,
  });
});

const deleteUser = asyncHandler(async (req: Request, res: Response) => {
  const user = await User.findOne();

  if (!user) {
    res.status(404);
    throw new Error("User do not exists");
  }

  const response = await User.deleteMany({});

  if (response.deletedCount === 0) {
    res.status(500);
    throw new Error("Failed to delete the user");
  }

  res.status(200).json({
    message: "User deleted successfully",
  });
});

export { getUserData, addUser, updateUser, deleteUser };
