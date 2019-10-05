import morpionEnv


def generate():
    morpion = morpionEnv.MorpionEnv(3, 0)
    morpion.generate_p()
    morpion.save_p("p.data")
generate()
