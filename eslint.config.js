import js from '@eslint/js';
import tsPlugin from '@typescript-eslint/eslint-plugin';
import tsParser from '@typescript-eslint/parser';
import prettierPlugin from 'eslint-plugin-prettier';
import prettierConfig from 'eslint-config-prettier';

export default [
	js.configs.recommended,
	{
		files: ['**/*.{js,jsx,ts,tsx}'],
		plugins: {
			'@typescript-eslint': tsPlugin,
			prettier: prettierPlugin,
		},
		languageOptions: {
			parser: tsParser,
			parserOptions: {
				ecmaVersion: 'latest',
				sourceType: 'module',
			},
			globals: {
				// Add Node.js globals here
				console: 'readonly',
				process: 'readonly',
				module: 'readonly',
				require: 'readonly',
				__dirname: 'readonly',
				__filename: 'readonly',
			},
		},
		rules: {
			...tsPlugin.configs.recommended.rules,
			...prettierPlugin.configs.recommended.rules,
			'prettier/prettier': 'error',
		},
	},
	prettierConfig,
];
