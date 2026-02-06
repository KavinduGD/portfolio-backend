import express from "express";
import {
  addProject,
  deleteProject,
  getProjects,
  updateProject,
} from "../controllers/projectController";
import adminValidator from "../middleware/authMiddleware";
import createUploader from "../utils/upload";

const projectImageUploader = createUploader("project", 5);

const router = express.Router();

router.get("/", getProjects);

router.post("/", adminValidator, projectImageUploader.any(), addProject);

router.patch("/:id", adminValidator, projectImageUploader.any(), updateProject);

router.delete("/:id", adminValidator, deleteProject);

export default router;
