import { createLocalVue } from "@vue/test-utils";
import Vuex from "vuex";

import { mount } from "@vue/test-utils";
import Mission from "@/views/Mission.vue";

const localVue = createLocalVue();
localVue.use(Vuex);
const store = new Vuex.Store({});

describe("Mission.vue", () => {
  it("checks textcontent", () => {
    const wrapper = mount(Mission);
    expect(wrapper.html()).toContain(h1);
  });
});
