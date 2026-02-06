import mongoose from "mongoose";
import { IProject } from "../types/types";

const projectSchema = new mongoose.Schema<IProject>({
  projectName: { type: String, required: true },
  projectDescription: { type: String, required: true },
  startedDate: { type: String, required: true },
  technologies: [{ type: String, required: true }],
  projectImages: [{ type: String, required: true }],
  links: [
    {
      linkName: { type: String, required: true },
      link: { type: String, required: true },
    },
  ],
  architectureImages: [
    {
      diagramName: { type: String, required: true },
      imageName: { type: String, required: true },
    },
  ],
  architectureDescription: { type: String, required: true },
  tags: [{ type: String, required: true }],
  score: { type: Number, required: true },
});

const Project = mongoose.model<IProject>("Project", projectSchema);

export default Project;
