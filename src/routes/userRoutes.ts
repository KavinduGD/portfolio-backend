import express from "express";
import { getUserData, addUser } from "../controllers/userController";

const router = express.Router();

router.get("/", getUserData);
router.post("/", addUser);

export default router;
