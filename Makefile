CLASS ?= 

manim: ./media/videos/main/480p15/$(CLASS).mp4

./media/videos/main/480p15/%.mp4: ./maths/manim.py
	manim -pql ./maths/manim.py $*

clean-windows:
	powershell -NoProfile -Command "if (Test-Path './media') { Remove-Item './media' -Recurse -Force }"

.PHONY: manim clean-windows
