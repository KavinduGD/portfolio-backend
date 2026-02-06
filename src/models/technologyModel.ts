import mongoose from "mongoose";
import { ITechnology } from "../types/types";

const technologySchema = new mongoose.Schema<ITechnology>({
  technology: {
    type: String,
    required: true,
    unique: true,
  },
  level: {
    type: Number,
    required: true,
  },
  icon: {
    type: String,
    required: true,
    unique: true,
  },
  type: {
    type: String,
    required: true,
  },
});

const Technology = mongoose.model<ITechnology>("Technology", technologySchema);

export default Technology;
/* 
technology
level
icon
type
*/

/* 
programming
    python
    javascript
    java
    Typescript

Web development
    HTML
    CSS
    React
    Express
    Flask
    Wordpress
    api Documentation (Openapi)

Devops
    docker 
    kubernetes 
    Github
    Github actions
    Jenkins
    Ansible
    Terraform
    Gitlab CI Cd
    AWS codepipeline

AI/ML
    Machine learning
    Deep learning
    AI agents

Designing/ Diagramming
    Figma
    Lucid chart
    Draw.io
    
Cloud 
    AWS
    Azure

Database 
    Mqsql
    Mongodb

 Linux
    linux commands
    bash scripting









*/
