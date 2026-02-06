import express from "express";
import {
  getUserData,
  addUser,
  updateUser,
  deleteUser,
} from "../controllers/userController";
import adminValidator from "../middleware/authMiddleware";

const router = express.Router();

router.get("/", getUserData);
router.post("/", adminValidator, addUser);
router.patch("/", adminValidator, updateUser);
router.delete("/", adminValidator, deleteUser);

export default router;
