function addUp(n) {
    return n > 1 ? n + addUp(n - 1) : 1;
}