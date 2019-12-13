import Resort from '@/components/Resort'
import Vue from 'vue'

describe('Resort.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Resort)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('h1').textContent)
      .to.equal('Keystone')
  })
})
