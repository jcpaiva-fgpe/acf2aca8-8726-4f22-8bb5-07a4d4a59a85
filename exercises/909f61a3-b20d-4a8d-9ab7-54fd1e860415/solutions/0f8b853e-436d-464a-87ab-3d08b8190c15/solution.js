function oddishOrEvenish(n) {
    return `${n}`.split('').reduce((a, b) => +a + (+b), 0) % 2 === 0 ? 'Evenish' : 'Oddish';
}