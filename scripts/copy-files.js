import { copyFile } from 'fs/promises';
import { join } from 'path';

async function copyFiles() {
  try {
    await copyFile('_headers', join('dist', '_headers'));
    await copyFile('_redirects', join('dist', '_redirects'));
    console.log('Files copied successfully');
  } catch (error) {
    console.error('Error copying files:', error);
    process.exit(1);
  }
}

copyFiles(); 