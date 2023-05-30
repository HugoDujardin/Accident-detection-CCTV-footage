sleep 40 
python3 /home/admin/Desktop/systemeIntelligent-main/Accident-detection-CCTV-footage-main/DéverrouillageSIM/déverrouillageSIM.py
sleep 10
sudo pon rnet
sleep 10 
sudo route add -net 0.0.0.0 ppp0
sleep 10
workon SystemeIntelligent
sleep 1
#python3 "/home/admin/Desktop/systemeIntelligent-main/Accident-detection-CCTV-footage-main/Accident_video.py"
