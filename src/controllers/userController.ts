import { Request, Response } from "express";
import asyncHandler from "express-async-handler";

const getUserData = asyncHandler(async (req: Request, res: Response) => {
  throw new Error("Function not implemented.");

  res.send("ass");
});

export { getUserData };
