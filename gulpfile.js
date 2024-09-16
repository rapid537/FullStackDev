const gulp = require('gulp')
const changed = require('gulp-changed')
const compile_less = require('gulp-less')
const concat = require('gulp-concat')
const minify = require('gulp-clean-css')

// *******************************************************
// Gulp will create a single minified .css file
// This file is imported into the root /src/index.js file
// All app styles are inherited from there
//
// Watching for changes to *.less
// *******************************************************

const SOURCE_LESS = './src/**/*.less'
const DESTINATION_CSS = './src/styles'

gulp.task('less', async function() {
    gulp.src(SOURCE_LESS)
    .pipe(concat('studio.css'))
    .pipe(compile_less())
    .pipe(minify())
    .pipe(changed(SOURCE_LESS))
    .pipe(gulp.dest(DESTINATION_CSS))
})

gulp.task('watch', function() {
    gulp.watch(SOURCE_LESS, gulp.series(['less']))
})

gulp.task('default', gulp.series(['watch']))
