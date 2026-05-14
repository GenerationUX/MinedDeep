import { QuartzConfig } from "./quartz-src/quartz/cfg"
import * as Plugin from "./quartz-src/quartz/plugins"

/**
 * MinedDeep — Quartz v4 configuration
 * Hassabis intellectual corpus wiki
 *
 * Content root: wiki/          (pass --directory wiki to quartz build)
 * Home page:    wiki/index.md  (rename _index.md → index.md once)
 * Pages:        wiki/pages/    (flat, slug-named)
 */

const config: QuartzConfig = {
  configuration: {
    pageTitle: "MinedDeep",
    pageTitleSuffix: " · Hassabis Corpus",
    enableSPA: true,
    enablePopovers: true,

    analytics: null, // add { provider: "plausible" } etc. if you want

    locale: "en-GB",
    baseUrl: "generationux.github.io/MinedDeep", // update if you use a custom domain

    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      "_log.md",           // operation log — don't publish
      "_corpus_log.json",  // internal tracking — don't publish
    ],

    defaultDateType: "modified",

    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Fraunces",       // scholarly serif for titles
        body: "Source Serif 4",   // readable body
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f4",        // warm off-white
          lightgray: "#e8e4dc",
          gray: "#8c8070",
          darkgray: "#3d3530",
          dark: "#1a1410",
          secondary: "#5c4a3a",   // warm brown — DeepMind earthy
          tertiary: "#8b6914",    // amber accent
          highlight: "rgba(139, 105, 20, 0.10)",
          textHighlight: "#ffd70088",
        },
        darkMode: {
          light: "#16130f",
          lightgray: "#2a2420",
          gray: "#6b5f54",
          darkgray: "#c8c0b4",
          dark: "#f0ece4",
          secondary: "#c4a882",
          tertiary: "#d4a838",
          highlight: "rgba(212, 168, 56, 0.10)",
          textHighlight: "#b5890055",
        },
      },
    },
  },

  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents({
        // Show ToC for the long synthesis and period pages
        minEntries: 3,
        maxDepth: 3,
        collapseByDefault: true,
      }),
      Plugin.CrawlLinks({
        markdownLinkResolution: "shortest",
        prettyLinks: true,
        openLinksInNewTab: false,
        lazyLoad: false,
        externalLinkIcon: true,
      }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],

    filters: [
      Plugin.RemoveDrafts(),
    ],

    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
        rssLimit: 40,
        rssFullHtml: false,
        includeEmptyFiles: false,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
