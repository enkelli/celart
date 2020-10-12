import randomColor from 'randomcolor';


let COLORS = [
    "blue",
    "green",
    "gold",
    "red",
    "brown",
    "blueviolet",
    "cornsilk",
    "cyan",
]

export function ColorForState(index) {
    while (index >= COLORS.length) {
        COLORS.push(randomColor());
    }
    return COLORS[index];
}
