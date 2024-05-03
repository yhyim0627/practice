# drive method를 가지고 있는 자동차 객체를 정의
import matplotlib.pyplot as plt
import numpy as np

class Car:
  def __init__(self):
    self.acc = 0
    self.velocity = np.array([])
    self.distance = np.array([])
  
  def drive(self, acc, d_time):
    self.acc = acc
    v = 0
    d = 0
    t = np.linspace(0, d_time, 1000)
    dt = t[1] - t[0]  # 시간 간격 계산
    for _ in t:
      v += acc * dt  # 속도 계산
      d += v * dt  # 거리 계산
      self.velocity = np.append(self.velocity, v)  # 속도 배열에 추가
      self.distance = np.append(self.distance, d)  # 거리 배열에 추가
    
    plt.plot(t, self.velocity)
    plt.title("Velocity vs Time")
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    plt.show()
    
    plt.plot(t, self.distance)
    plt.title("Distance vs Time")
    plt.xlabel("Time")
    plt.ylabel("Distance")
    plt.show()

#acc : 자동차의 입력 가속도(Acceleration), d_time : 자동차의 주행 시간(Driving-time)
acc, d_time = map(int, input().split()) 

# 자동차 객체 생성
my_car = Car()

# drive 메소드 호출
my_car.drive(acc, d_time)
