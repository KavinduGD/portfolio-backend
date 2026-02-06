import express from "express";
import {
  addTechnology,
  getAllTechnologies,
  updateTechnology,
  deleteTechnology,
} from "../controllers/technologyController";
import createUploader from "../utils/upload";
import adminValidator from "../middleware/authMiddleware";

const technologyImageUploader = createUploader("technology", 5);

const router = express.Router();

router.get("/", getAllTechnologies);

router.post(
  "/",
  adminValidator,
  technologyImageUploader.single("tech-icon-image"),
  addTechnology,
);

router.patch(
  "/:id",
  adminValidator,
  technologyImageUploader.single("tech-icon-image"),
  updateTechnology,
);

router.delete("/:id", adminValidator, deleteTechnology);

export default router;
