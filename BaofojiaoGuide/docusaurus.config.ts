import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

const config: Config = {
  title: '抱佛脚 Guide',
  tagline: 'CIE IGCSE / AS / A Level 临时抱佛脚复习指南',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://baofojiao-guide.vercel.app',
  baseUrl: '/',

  organizationName: 'baofojiao',
  projectName: 'baofojiao-guide',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'zh-Hans',
    locales: ['zh-Hans'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          routeBasePath: '/',
          numberPrefixParser: false,
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/og-image.png',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: '抱佛脚 Guide',
      logo: {
        alt: 'Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'mainSidebar',
          position: 'left',
          label: 'Subjects',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/anomalyco/BaofojiaoGuide',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Introduction',
              to: '/intro',
            },
            {
              label: 'How to Use This Site',
              to: '/guide/how-to-use-this-site',
            },
            {
              label: 'Exam Strategy',
              to: '/guide/exam-strategy',
            },
          ],
        },
        {
          title: 'Subjects',
          items: [
            {
              label: '9702 Physics',
              to: '/subjects/9702-physics',
            },
            {
              label: '9231 Further Mathematics',
              to: '/subjects/9231-further-mathematics',
            },
            {
              label: '9618 Computer Science',
              to: '/subjects/9618-computer-science/paper-3',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/anomalyco/BaofojiaoGuide',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} 抱佛脚 Guide. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
