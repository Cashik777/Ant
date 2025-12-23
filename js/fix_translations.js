const fs = require('fs');
const path = 'C:/Users/Dgello/.gemini/antigravity/scratch/EthioDirect/js/translations.js';
const content = fs.readFileSync(path, 'utf8');
const lines = content.split(/\r?\n/);

console.log('Original lines:', lines.length);

// 1. Cut the mess
const cleanLines = [
    ...lines.slice(0, 2337),
    '    },',
    ...lines.slice(2756)
];

console.log('Cleaned lines:', cleanLines.length);

// 2. Fix indentation
let depth = 0;
const formattedLines = cleanLines.map((line, index) => {
    let trimmed = line.trim();
    if (!trimmed) return '';

    // Adjust depth for closing braces at the start of the line
    // Special case for window.LOCALES = {
    if (index === 0) {
        let res = trimmed;
        if (trimmed.endsWith('{')) depth = 1;
        return res;
    }

    if (trimmed.startsWith('}') || trimmed.startsWith(']')) {
        depth = Math.max(0, depth - 1);
    }

    const result = '    '.repeat(depth) + trimmed;

    if (trimmed.endsWith('{') || trimmed.endsWith('[')) {
        depth += 1;
    }

    return result;
});

fs.writeFileSync(path, formattedLines.join('\n'));
console.log('File fixed and saved.');
