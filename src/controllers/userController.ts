import { Request, Response } from "express";
import asyncHandler from "express-async-handler";
import User from "../models/userModel";

const getUserData = asyncHandler(async (req: Request, res: Response) => {
  const user = await User.findOne();

  if (user) {
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
    password,
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
    !password ||
    !about ||
    !age ||
    !address ||
    !languages ||
    !phone ||
    !jobTitle ||
    !education
  ) {
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
    password,
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

export { getUserData, addUser };
