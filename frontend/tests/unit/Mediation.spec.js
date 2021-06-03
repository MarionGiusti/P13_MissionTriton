import { shallowMount, createLocalVue  } from "@vue/test-utils";
import Mediation from "@/views/Mediation";
import Vuetify from'vuetify'
import Vuex from 'vuex'

const localVue = createLocalVue()
localVue.use(Vuex)

describe("Mediation", () => {
  let vuetify

  beforeEach(() => {
    vuetify = new Vuetify()
  })

  it("checks textcontent", () => {
    const wrapper = shallowMount(Mediation, {
      localVue,
      vuetify,
    });
    expect(wrapper.html()).toContain("Médiation");    
  });
});
