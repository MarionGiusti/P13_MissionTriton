import { shallowMount, createLocalVue  } from "@vue/test-utils";
import VueRouter from 'vue-router'
import NavLink from "@/components/NavLink";
import Vuetify from'vuetify'
import Vue from 'vue'

// const localVue = createLocalVue()
// localVue.use(VueRouter)


describe("NavLink component unit tests: ", () => {

  const localVue = createLocalVue()
  let vuetify

  const router = new VueRouter()

  const $route = {
    path: '/some/path'
  }

  const $store = {
    state: {
      token: null,
      userID: null,
      userDetails: {},
    },
    getters: {
      currentMission: () => {}
    }
  }

  beforeEach(() => {
    vuetify = Vue.use(Vuetify)
  })

  it("find login button", () => {
    const wrapper = shallowMount(NavLink, {
      localVue,
      vuetify,
      router,
      mocks: {
        $route: {
          params: {
            id: ''
          }
        },
        $store
      }
    });
    // wrapper.setData({ id: "" });
    const button = wrapper.find("v-btn");
    button.trigger("click");
    expect(window.location.href).toBeTrue;
    // expect(wrapper.html()).toContain('');
  });
  
  // it('it\'s a vue instance', () => {
  // const wrapper = ShallowMount(NavLink);
  // expect(wrapper.IsVueInstance()).toBeTruthy();
  // });
});
