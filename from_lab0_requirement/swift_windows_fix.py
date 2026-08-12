import os
import importlib.util

def apply():
    if os.name != "nt":
        return "skipped"

    spec = importlib.util.find_spec("swift")
    if spec is None or not spec.origin:
        return "skipped"

    route = os.path.join(os.path.dirname(spec.origin), "SwiftRoute.py")
    if not os.path.exists(route):
        return "skipped"

    with open(route, encoding="utf-8") as handle:
        source = handle.read()

    guard = (
        'if os.name == "nt" and len(self.path) > 2 '
        'and self.path[0] == "/" and self.path[2] == ":":'
    )

    if guard in source:
        return "already"

    marker = "self.path = urllib.parse.unquote(self.path[9:])"
    if marker not in source:
        print(
            "[warn] SwiftRoute.py has an unexpected layout, so the Windows "
            "mesh-path fix was skipped. If your robot's meshes do not appear, "
            "tell your instructor."
        )
        return "skipped"

    replacement = (
        marker
        + "\n" + " " * 20 + guard
        + "\n" + " " * 24 + "self.path = self.path[1:]"
    )
    source = source.replace(marker, replacement, 1)

    with open(route, "w", encoding="utf-8") as handle:
        handle.write(source)

    print("[ok] applied Windows mesh-path fix to SwiftRoute.py")
    return "patched"


if __name__ == "__main__":
    result = apply()
    messages = {
        "patched": "Fix applied. Swift will now load robot meshes on Windows.",
        "already": "Fix was already present. Nothing to do.",
        "skipped": "Nothing to do on this platform (or Swift not found).",
    }
    print(messages.get(result, result))