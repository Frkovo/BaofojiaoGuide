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

  markdown: {
    mermaid: true,
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
          label: '科目',
        },
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
          title: '文档',
          items: [
            {
              label: '首页',
              to: '/',
            },
            {
              label: '如何使用本站',
              to: '/guide/how-to-use-this-site',
            },
            {
              label: '通用考试策略',
              to: '/guide/exam-strategy',
            },
          ],
        },
        {
          title: '科目',
          items: [
            {
              label: '9702 物理学',
              to: '/subjects/9702-physics',
            },
            {
              label: '9231 进阶数学',
              to: '/subjects/9231-further-mathematics',
            },
            {
              label: '9618 计算机科学',
              to: '/subjects/9618-computer-science/paper-3',
            },
          ],
        },
        {
          title: '更多',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/anomalyco/BaofojiaoGuide',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} 抱佛脚 Guide. Built with Docusaurus. 作者: Deepseek V4 Flash`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
  themes: ['@docusaurus/theme-mermaid'],
};

export default config;
