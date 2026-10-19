from vpython import

# Create scene
scene.title = "Rotatable Earth"
scene.width = 1000
scene.height = 800
scene.background = color.black

# Create Earth sphere
earth = sphere(
    radius=2,
    texture=textures.earth
)

# Add light
local_light(pos=vector(5,5,5), color=color.white)

# Slow automatic rotation
while True:
    rate(60)
    earth.rotate(angle=0.01, axis=vector(0,1,0))