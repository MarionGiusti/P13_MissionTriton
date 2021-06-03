import { shallowMount } from "@vue/test-utils";
import HomeMission from "@/views/HomeMission.vue";

describe("HomeMission", () => {
  it("checks textcontent", () => {
    const wrapper = shallowMount(HomeMission);
    expect(wrapper.html()).toContain("Actu");
    expect(wrapper.html()).toContain("Where is the ship ?");
  });
});
