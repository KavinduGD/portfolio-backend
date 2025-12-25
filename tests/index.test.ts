import { add } from "../src";

describe("add function", () => {
  test("adds two numbers correctly", () => {
    const result = add(2, 3);
    expect(result).toBe(5);
  });
});
