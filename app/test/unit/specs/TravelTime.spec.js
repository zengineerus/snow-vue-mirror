// import TravelTime from '@/components/TravelTime'
import Resort from '@/components/Resort'
import Vue from 'vue'
// import Sinon from 'sinon'
// import SnowVueService from '@/services/snow-data'
// import { mount, shallowMount } from '@vue/test-utils'

describe('TravelTime.vue', () => {
  it('should render a Not Available error message', () => {
    const Constructor = Vue.extend(Resort)
    const vm = new Constructor().$mount()
    console.log('dfaslkjasf;lkjadfs;lkjfas', vm.$el.querySelector('#new-snow'));
    // expect(vm.$el.querySelector('#travelTimeMessage').textContent).to.equal('Data is not available.')
  })
})
