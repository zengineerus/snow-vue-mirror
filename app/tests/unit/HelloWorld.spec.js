import { shallowMount } from '@vue/test-utils'
import HelloWorld from '@/components/HelloWorld'

describe('HelloWorld.vue', () => {
  test('should render correct contents', () => {
    const wrapper = shallowMount(HelloWorld);
    expect(wrapper.isVueInstance()).toBeTruthy();
    expect(wrapper.find('.hello h1').text()).toBe('Welcome to Your Vue.js App');
  })
})
