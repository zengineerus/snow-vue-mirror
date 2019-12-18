import { shallowMount } from '@vue/test-utils';
import Resort from '@/components/Resort';

jest.mock('@/services/snow-data', () => ({ 
  snowReports: () => Promise.resolve({body: 'test snow report'}),
  travelTime: () => Promise.resolve({body: 'test travel time'})
}));

describe('Resort.vue', () => {
  test('should render correct contents', () => {
    const wrapper = shallowMount(Resort);
    expect(wrapper.isVueInstance()).toBeTruthy();
    expect(wrapper.find('h1').text()).toBe('Keystone');
    // expect(wrapper.text()).toContain('test snow report');
    // expect(wrapper.text()).toContain('test travel time');
  });
});
