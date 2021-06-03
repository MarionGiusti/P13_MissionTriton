import { shallowMount, createLocalVue  } from "@vue/test-utils";
import NavLink from "@/components/NavLink";
import Vuetify from'vuetify'

describe("NavLink component unit tests: ", () => {
  const localVue = createLocalVue()
  let vuetify

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
    vuetify = new Vuetify()
  })

  it("find login button", () => {
    const wrapper = shallowMount(NavLink, {
      localVue,
      vuetify,
      mocks: {
        $route: {
          params: {
            id: ''
          }
        },
        $store
      }
    });

    const button = wrapper.find("v-btn");
    expect(button.exists()).toBeTrue;
  });
});
