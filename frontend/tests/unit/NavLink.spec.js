// import { mount } from '@vue/test-utils'
import NavLink from '@/components/NavLink'
import { shallowMount } from '@vue/test-utils'

describe('NavLink component unit tests: ', () => {
//   // it('it\'s a vue instance', () => {
//   //   const wrapper = mount(NavLink);
//   //   expect(wrapper.IsVueInstance()).toBeTruthy();
//   // });

  it('find login button', () => {
    const wrapper = shallowMount(NavLink, {
      data() {
        return {
          id: '',
        }
      }
    });
    wrapper.setData({id: ''})
    const button = wrapper.find('button');
    button.trigger('click')
    expect(window.location.href).toBe('/login');
    // expect(wrapper.html()).toContain(button);
  });


  
//     //   // vérifie que `message` est restitué
//     //   expect(wrapper.find('.message').text()).toEqual('Hello World')
  
//     //   // vérifie que `error` est restituée
//     //   expect(wrapper.find('.error').exists()).toBeTruthy()
  
//     //   // met à jour `username` et vérifie que `error` n'est plus restituée
//     //   wrapper.setData({ username: 'Lachlan' })
//     //   expect(wrapper.find('.error').exists()).toBeFalsy()
//     // })
    
  })
