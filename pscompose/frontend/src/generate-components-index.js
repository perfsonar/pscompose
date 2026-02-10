const fs = require('fs');
const path = require('path');

const dirPath = './components';
const outputFile = path.join(dirPath, 'index.js');

// Read directory
fs.readdir(dirPath, (err, files) => {
    if (err) {
        console.error('Error reading directory:', err);
        return;
    }

    // Filter ps-*.js files (exclude index.js)
    const componentFiles = files.filter(file => 
        file.startsWith('ps-') && 
        file.endsWith('.js') && 
        file !== 'index.js'
    );

    if (componentFiles.length === 0) {
        console.log('No ps-*.js files found');
        return;
    }

    // Generate dynamic imports + auto-registration
    const importStatements = componentFiles.map(file => `import '/components/${file}';`).join('\n    ');

    const content = 
    `
    /* AUTO-GENERATED — DO NOT EDIT */
    ${importStatements}

    // Export component names list too
    export const componentNames = [
        ${componentFiles.map(f => `"${f.slice(0, -3)}"`).join(',\n        ')}
    ];

    export default componentNames;
    `;


    fs.writeFile(outputFile, content, (err) => {
        if (err) {
        console.error('Error writing index.js:', err);
        } else {
        console.log(`✅ Generated auto-registration for ${componentFiles.length} components!`);
        }
    });
});
