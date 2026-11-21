/**
 * Returns a property descriptor for a string HTML attribute.
 * Usage: Object.defineProperty(MyEl.prototype, "label", attr("label"));
 */
export function attr(name) {
    return {
        configurable: true,
        get() {
            return this.getAttribute(name) ?? "";
        },
        set(v) {
            this.setAttribute(name, v ?? "");
        },
    };
}

/**
 * Returns a property descriptor for a boolean HTML attribute (presence = true).
 * Usage: Object.defineProperty(MyEl.prototype, "disabled", boolAttr("disabled"));
 */
export function boolAttr(name) {
    return {
        configurable: true,
        get() {
            return this.hasAttribute(name);
        },
        set(v) {
            v ? this.setAttribute(name, "") : this.removeAttribute(name);
        },
    };
}

/**
 * Returns a property descriptor for an attribute that returns null when absent.
 * Usage: Object.defineProperty(MyEl.prototype, "min", nullableAttr("min"));
 */
export function nullableAttr(name) {
    return {
        configurable: true,
        get() {
            return this.getAttribute(name) ?? null;
        },
        set(v) {
            this.setAttribute(name, v ?? "");
        },
    };
}
