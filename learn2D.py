import sketch

texture = sketch.sketch()

texture.learn()

new_Texture = texture.sample()

sketch.paint(new_Texture)