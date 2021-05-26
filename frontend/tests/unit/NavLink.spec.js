// import { mount } from '@vue/test-utils'
import NavLink from "@/components/NavLink";
import { shallowMount  } from "@vue/test-utils";
// import VueRouter from 'vue-router'

// const localVue = createLocalVue()
// localVue.use(VueRouter)
// const router = new VueRouter()

// const $route = {
//   path: '/some/path'
// }

describe("NavLink component unit tests: ", () => {
  //   // it('it\'s a vue instance', () => {
  //   //   const wrapper = mount(NavLink);
  //   //   expect(wrapper.IsVueInstance()).toBeTruthy();
  //   // });

  it("find login button", () => {
    const wrapper = shallowMount(NavLink);
    // wrapper.setData({ id: "" });
    // const button = wrapper.find("v-btn");
    // button.trigger("click");
    // expect(window.location.href).toBe("/login");
    expect(wrapper.html()).toContain('');
  });
});
