import { mount } from '@vue/test-utils';
import SnowFall from '@/components/SnowFall';
import Vue from 'vue'

jest.mock('@/services/snow-data', () => ({ 
    travelTime: jest.fn(),
    snowReports: () => Promise.resolve({
        body: {
            SnowReport: [
                {
                    Depth: 
                    {
                        Inches: 11
                    }
                },
                {
                    Depth:
                    {
                        Inches: 22
                    }
                }
            ]
        }
    })
}));

describe('SnowFall.vue', () => {
    test('should show snow data', async() => {

        const wrapper = mount(SnowFall);
        expect(wrapper.isVueInstance()).toBeTruthy();
        await Vue.nextTick();

        expect(wrapper.text()).toContain('Overnight SnowFall 24 Hour Snow 11 inches 22 inches');
    })
});