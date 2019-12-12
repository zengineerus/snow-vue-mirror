from PIL import Image, ImageDraw, ImageFont
import urllib.request as urllib
from datetime import datetime, date, timedelta
from dateutil import tz


def round_time(time, base=5):
    return round(time/base) * base


def image_request(url, time):
    try:
        request = urllib.Request(url)
        response = urllib.urlopen(request)
        if response.status == 200:
            image = Image.open(response)
            draw = ImageDraw.Draw(image)
            time = time.replace(tzinfo=tz.tzutc())
            local_time = time.astimezone(tz.tzlocal())
            local_time = local_time.strftime("%Y-%m-%d %I:%M %p")
            font = ImageFont.truetype(
                "Arial Bold.ttf", 20, index=0, encoding="armn")
            # font = ImageFont.truetype('arial.ttf', 15)
            draw.text((10, 10), str(local_time),
                      fill=(0, 0, 255, 255), font=font)
            return image
        else:
            return None
    except Exception as e:
        print(url, str(e))
        return None


frames = []

time = datetime.utcnow()
start = time - timedelta(hours=4)
stop = time
images = []
while start <= stop:
    url = "https://timecam.tv/mediablock/timestreams/vailresort/keystone-snowcam/hour/{date}_{hour}/keystone-snowcam_{date}_{hour}_{minute}_00_00.jpg"
    date = f"{start.year}_{start.month}_{start.day}"
    hour = start.hour
    minute = round_time(start.minute)
    if hour < 10:
        hour = '0' + str(hour)
    if minute < 10:
        minute = '0' + str(minute)

    url = url.format(date=date, hour=hour, minute=minute)
    image = image_request(url, start)
    if image is not None:
        images.append(image)

    start += timedelta(minutes=5)
print(len(images))
timestamp = int(stop.timestamp())

filepath = f"../../app/images/keystone_snow_stake_{timestamp}.gif"
images[0].save(filepath, format='GIF',
               append_images=images[1:], save_all=True, duration=500, loop=0)
