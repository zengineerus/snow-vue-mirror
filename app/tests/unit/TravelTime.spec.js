import { mount } from '@vue/test-utils';
import TravelTime from '@/components/TravelTime';
import Vue from 'vue';
import { travelTime } from '@/services/snow-data';

jest.mock('@/services/snow-data', () => ({ 
    travelTime: jest.fn(),
    getCurrentLocation: () => Promise.resolve({
        body: {
            Location: {
                zip: 12345
            },
        }
    })
}));

describe('TravelTime.vue', () => {
    beforeEach(() => jest.resetModules());

    test('should show travel time', async() => {
        travelTime.mockImplementation(() => Promise.resolve({
            body: {
                TrafficReport: {
                    travel_time: {
                        hours: 1,
                        minutes: 13
                    }
                }
            }
        }));

        const wrapper = mount(TravelTime);
        expect(wrapper.isVueInstance()).toBeTruthy();
        await Vue.nextTick();

        expect(wrapper.text()).toContain('1 hours 13 minutes');
    })

    test('should show travel time error message', async() => {
        travelTime.mockImplementation(() => Promise.resolve({
                body: {           
                    message: "test travel time"}
                }));

        const wrapper = mount(TravelTime);
        expect(wrapper.isVueInstance()).toBeTruthy();
        await Vue.nextTick();
        expect(wrapper.text()).toContain('Server is unavailable.');
    })
})
