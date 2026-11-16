import { defineConfig } from 'vite';
import dts from 'vite-plugin-dts';
import { resolve } from 'path';
import postcss from 'postcss';
import fs from 'fs';
import cssnano from 'cssnano';

const processCSSFile = (inputPath: string, outputPath: string) => {
	fs.readFile(inputPath, (err, css) => {
		if (err) throw err;

		// Ensure output directory exists
		const outputDir = resolve(outputPath, '..');
		if (!fs.existsSync(outputDir)) {
			fs.mkdirSync(outputDir, { recursive: true });
		}

		postcss([cssnano({ preset: 'default' })])
			.process(css, { from: inputPath, to: outputPath })
			.then((result) => {
				fs.writeFile(outputPath, result.css, () => true);
				if (result.map) {
					fs.writeFile(outputPath + '.map', result.map.toString(), () => true);
				}
			});
	});
};

const FONT_FILES = [
	'InterVariable-latin.woff2',
	'InterVariable-rest.woff2',
	'LICENSE.txt',
	'GeistMonoVariable-latin.woff2',
	'GeistMonoVariable-rest.woff2',
	'LICENSE-GeistMono.txt',
];

const FONT_STYLESHEETS = ['inter.css', 'geist-mono.css'];

const copyFonts = () => {
	const fontsDir = resolve(__dirname, 'src/fonts');
	const outputDir = resolve(__dirname, 'dist/fonts');

	fs.mkdirSync(outputDir, { recursive: true });
	FONT_FILES.forEach((file) => {
		fs.copyFileSync(resolve(fontsDir, file), resolve(outputDir, file));
	});
	FONT_STYLESHEETS.forEach((file) => {
		processCSSFile(resolve(fontsDir, file), resolve(outputDir, file));
	});
};

export default defineConfig({
	build: {
		lib: {
			entry: resolve(__dirname, 'src/index.ts'),
			name: 'designTokens',
			fileName: 'design-tokens',
		},
		rollupOptions: {
			external: [],
		},
	},
	plugins: [
		dts({
			include: ['src/**/*'],
			outDirs: 'dist',
			bundleTypes: true,
		}),
		{
			name: 'copy-css',
			writeBundle() {
				// Process both CSS files
				processCSSFile(
					resolve(__dirname, 'src/style.css'),
					resolve(__dirname, 'dist/style.css'),
				);
				processCSSFile(
					resolve(__dirname, 'src/tailwind-theme.css'),
					resolve(__dirname, 'dist/tailwind-theme.css'),
				);
				processCSSFile(
					resolve(__dirname, 'src/themes/signoz-tokens.css'),
					resolve(__dirname, 'dist/themes/signoz-tokens.css'),
				);
				processCSSFile(
					resolve(__dirname, 'src/Typography/typography-styles.css'),
					resolve(__dirname, 'dist/Typography/typography-styles.css'),
				);
				// Opt-in Inter and Geist Mono faces, loaded only by a consumer that imports their stylesheet
				copyFonts();
			},
		},
	],
});
