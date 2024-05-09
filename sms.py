import cv2
import requests


def send_sms(message):
  
    api_key = 'your_api_key'
    api_secret = 'your_api_secret'
    from_number = 'your_sender_number'
    to_number = 'recipient_number'

    url = f'https://rest.nexmo.com/sms/json'


    data = {
        'api_key': 'f806351b',
        'api_secret': 'tGAOIgssub8NVTkP',
        'from': 'Vonage APIs',
        'to': '919871740250',
        'text': 'A Humen has been detected please Check '
    }
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("SMS sent successfully!")
    else:
        print(f"Failed to send SMS: {response.text}")

def detect_motion(frame1, frame2):

    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        message = "Movement detected!"
        send_sms(message)

def main():
    cap = cv2.VideoCapture(0)

    _, frame1 = cap.read()
    _, frame2 = cap.read()

    while cap.isOpened():
        _, frame3 = cap.read()

        detect_motion(frame1, frame3)

        frame1 = frame2
        frame2 = frame3

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
