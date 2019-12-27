import { mount } from '@vue/test-utils';
import SnowFall from '@/components/SnowFall';
import Vue from 'vue'
import { snowReport } from '@/services/snow-data';

jest.mock('@/services/snow-data', () => ({ 
    snowReport: jest.fn()
}));

describe('SnowFall.vue', () => {
    beforeEach(() => jest.resetModules());

    test('should show snow data', async() => {
        snowReport.mockImplementation(() => Promise.resolve({
            body: 
            {
                SnowReport: 
                [
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
        }));
        const wrapper = mount(SnowFall);
        expect(wrapper.isVueInstance()).toBeTruthy();

        await Vue.nextTick();

        expect(wrapper.text()).toContain('Overnight SnowFall 24 Hour Snow 11 in 22 in');
    });

    test('should show error when can\'t retrieve snow data', async() => {
        snowReport.mockImplementation(() => Promise.reject({}));
        const wrapper = mount(SnowFall);
        expect(wrapper.isVueInstance()).toBeTruthy();
        
        await Vue.nextTick();

        expect(wrapper.text()).toContain('Data is not available.');
    });



});
