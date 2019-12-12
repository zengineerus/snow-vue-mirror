import Vue from 'vue'
import HelloWorld from '@/components/resort'

describe('Resort.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(HelloWorld)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('h1').textContent)
      .to.equal('Keystone')
  })
})
