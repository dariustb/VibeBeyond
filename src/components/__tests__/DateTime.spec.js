import { describe, it, expect } from "vitest";

import { mount } from "@vue/test-utils";
import DateTime from "../DateTime.vue";

describe("DateTime", () => {
  it("returns a non-empty string", () => {
    const wrapper = mount(DateTime);
    expect(wrapper.text()).not.toHaveLength(0);
  });
  it("doesn't show placeholder time & date", () => {
    const wrapper = mount(DateTime);
    expect(wrapper.text()).not.toContain("OCTOBER 06 1989");
    expect(wrapper.text()).not.toContain("PM 7:07");
  });
});
