import model 

m = model.Model()

print ("default model: {}".format(m))

print("#### Setting a speed to motor 1 only")
m.m1.speed = 0.1
m.m2.speed = 0.1
print("\n#########\nmodel: {}".format(m))
linear_speed, rotation_speed = m.dk()
print ("linear_speed,={}\nrotational_speed={}".format(linear_speed, rotation_speed))


print("#### Setting opposed speed for both motors")
m.m1.speed = 0.1
m.m2.speed = 0.2
print("\n#########\nmodel: {}".format(m))
linear_speed, rotation_speed = m.dk()
print ("linear_speed,={}\nrotational_speed={}".format(linear_speed, rotation_speed))

print("#### Setting speed2 = 2xspeed1")
m.m1.speed = 0.1
m.m2.speed = 0.2
print("\n#########\nmodel: {}".format(m))
linear_speed, rotation_speed = m.dk()
print ("linear_speed,={}\nrotational_speed={}".format(linear_speed, rotation_speed))