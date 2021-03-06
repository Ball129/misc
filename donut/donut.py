# Esteban Garcia-Gurtubay Jan 2014

import math


def render_frame(a, b):
    # Precompute sines and cosines of A and B
    cos_a = math.cos(a)
    sin_a = math.sin(a)
    cos_b = math.cos(b)
    sin_b = math.sin(b)

    char_output = []
    zbuffer = []

    # noinspection PyShadowingNames
    for i in range(screen_height + 1):
        char_output.append([' '] * (screen_width + 0))
        zbuffer.append([0.0] * (screen_width + 0))

    # theta goes around the cross-sectional circle of a torus
    theta = 0
    while theta < 2 * math.pi:
        theta += theta_spacing

        # Precompute sines and cosines of theta
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)

        # phi goes around the center of revolution of a torus
        phi = 0
        while phi < 2 * math.pi:
            phi += phi_spacing

            # Precompute sines and cosines of phi
            cos_phi = math.cos(phi)
            sin_phi = math.sin(phi)

            # the x,y coordinate of the circle,
            # before revolving (factored out of the above equations)
            circle_x = R2 + R1 * cos_theta
            circle_y = R1 * sin_theta

            # final 3D (x,y,z) coordinate after rotations, directly from our math above
            x = circle_x * (cos_b * cos_phi + sin_a * sin_b * sin_phi) - circle_y * cos_a * sin_b
            y = circle_x * (sin_b * cos_phi - sin_a * cos_b * sin_phi) + circle_y * cos_a * cos_b
            z = K2 + cos_a * circle_x * sin_phi + circle_y * sin_a
            ooz = 1 / z

            # x and y projection. y is negated here, because y goes up in
            # 3D space but down on 2D displays.
            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)

            # Calculate luminance
            luminance = cos_phi * cos_theta * sin_b - cos_a * cos_theta * sin_phi - sin_a * sin_theta + cos_b * (
                    cos_a * sin_theta - cos_theta * sin_a * sin_phi)

            # L ranges from -sqrt(2) to +sqrt(2).  If it's < 0, the surface is
            # pointing away from us, so we won't bother trying to plot it.
            if luminance > 0:
                # Test against the z-buffer. Larger 1/z means the pixel is closer to
                # the viewer than what's already plotted.
                if ooz > zbuffer[xp][yp]:
                    zbuffer[xp][yp] = ooz
                    luminance_index = luminance * 8  # this brings L into the range 0..11 (8*sqrt(2) = 11.3)

                    # Now we lookup the character corresponding
                    # to the luminance and plot it in our output
                    char_output[xp][yp] = '.,-~:;=!*#$@'[int(luminance_index)]

    # Now, dump char_output to the screen.
    # Bring cursor to "home" location, in just about any currently-used terminal emulation mode
    # print('\x1b[H')

    # Clear screen
    print('\033c')

    # noinspection PyShadowingNames
    for i in range(screen_height):
        print(''.join(char_output[i][:]))


theta_spacing = 0.07
phi_spacing = 0.02

R1 = 1
R2 = 2
K2 = 5

# Calculate K1 based on screen size: the maximum x-distance occurs roughly at
# the edge of the torus, which is at x=R1+R2, z=0.  we want that to be
# displaced 3/8ths of the width of the screen, which is 3/4th of the way from
# the center to the side of the screen.
# screen_width*3/8 = K1*(R1+R2)/(K2+0)
# screen_width*K2*3/(8*(R1+R2)) = K1

screen_width = 35
screen_height = 35

K1 = screen_width * K2 * 3 / (8 * (R1 + R2))

# print('\x1b[2J')
A = 1.0
B = 1.0

for i in range(250):
    render_frame(A, B)
    A += 0.08
    B += 0.03
