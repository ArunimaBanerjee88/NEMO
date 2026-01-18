def decide_next_task(letter, stage):

    if stage == "phonics":
        return (
            f"🎧 Today let’s listen to how **'{letter}'** sounds.\n"
            f"Say it slowly: **/{letter.lower()}/**",
            "writing"
        )

    elif stage == "writing":
        return (
            f"✍️ Now let’s practice writing **'{letter}'**.\n"
            f"Trace it in the air, then on paper.",
            "revision"
        )

    else:
        next_letter = chr(ord(letter) + 1)
        return (
            f"⭐ Great job! Tomorrow we’ll start with **'{next_letter}'**.",
            "phonics"
        )
