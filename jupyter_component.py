import streamlit as st
import streamlit.components.v1 as components
def data():
    components.html(
        r"""
        <style type="text/css">
        pre { line-height: 125%; }
    td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
    span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
    td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
    span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
    .highlight .hll { background-color: var(--jp-cell-editor-active-background) }
    .highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
    .highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
    .highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
    .highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
    .highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
    .highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
    .highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
    .highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
    .highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
    .highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
    .highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
    .highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
    .highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
    .highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
    .highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
    .highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
    .highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
    .highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
    .highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
    .highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
    .highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
    .highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
    .highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
    .highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
    .highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
    .highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
    .highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
    .highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
    .highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
    .highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
    .highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
    .highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
    .highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
    .highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
    .highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
    .highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
    .highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
    .highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
    .highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
    .highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
    .highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
    .highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
    </style>
    <style type="text/css">
    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*
    * Mozilla scrollbar styling
    */

    /* use standard opaque scrollbars for most nodes */
    [data-jp-theme-scrollbars='true'] {
    scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
        var(--jp-scrollbar-background-color);
    }

    /* for code nodes, use a transparent style of scrollbar. These selectors
    * will match lower in the tree, and so will override the above */
    [data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
    [data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
    scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
    }

    /* tiny scrollbar */

    .jp-scrollbar-tiny {
    scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
    scrollbar-width: thin;
    }

    /* tiny scrollbar */

    .jp-scrollbar-tiny::-webkit-scrollbar,
    .jp-scrollbar-tiny::-webkit-scrollbar-corner {
    background-color: transparent;
    height: 4px;
    width: 4px;
    }

    .jp-scrollbar-tiny::-webkit-scrollbar-thumb {
    background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
    }

    .jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
    border-left: 0 solid transparent;
    border-right: 0 solid transparent;
    }

    .jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
    border-top: 0 solid transparent;
    border-bottom: 0 solid transparent;
    }

    /*
    * Lumino
    */

    .lm-ScrollBar[data-orientation='horizontal'] {
    min-height: 16px;
    max-height: 16px;
    min-width: 45px;
    border-top: 1px solid #a0a0a0;
    }

    .lm-ScrollBar[data-orientation='vertical'] {
    min-width: 16px;
    max-width: 16px;
    min-height: 45px;
    border-left: 1px solid #a0a0a0;
    }

    .lm-ScrollBar-button {
    background-color: #f0f0f0;
    background-position: center center;
    min-height: 15px;
    max-height: 15px;
    min-width: 15px;
    max-width: 15px;
    }

    .lm-ScrollBar-button:hover {
    background-color: #dadada;
    }

    .lm-ScrollBar-button.lm-mod-active {
    background-color: #cdcdcd;
    }

    .lm-ScrollBar-track {
    background: #f0f0f0;
    }

    .lm-ScrollBar-thumb {
    background: #cdcdcd;
    }

    .lm-ScrollBar-thumb:hover {
    background: #bababa;
    }

    .lm-ScrollBar-thumb.lm-mod-active {
    background: #a0a0a0;
    }

    .lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
    height: 100%;
    min-width: 15px;
    border-left: 1px solid #a0a0a0;
    border-right: 1px solid #a0a0a0;
    }

    .lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
    width: 100%;
    min-height: 15px;
    border-top: 1px solid #a0a0a0;
    border-bottom: 1px solid #a0a0a0;
    }

    .lm-ScrollBar[data-orientation='horizontal']
    .lm-ScrollBar-button[data-action='decrement'] {
    background-image: var(--jp-icon-caret-left);
    background-size: 17px;
    }

    .lm-ScrollBar[data-orientation='horizontal']
    .lm-ScrollBar-button[data-action='increment'] {
    background-image: var(--jp-icon-caret-right);
    background-size: 17px;
    }

    .lm-ScrollBar[data-orientation='vertical']
    .lm-ScrollBar-button[data-action='decrement'] {
    background-image: var(--jp-icon-caret-up);
    background-size: 17px;
    }

    .lm-ScrollBar[data-orientation='vertical']
    .lm-ScrollBar-button[data-action='increment'] {
    background-image: var(--jp-icon-caret-down);
    background-size: 17px;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-Widget {
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
    }

    .lm-Widget.lm-mod-hidden {
    display: none !important;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    .lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
    /* Title is rotated for horizontal accordion panel using CSS */
    display: block;
    transform-origin: top left;
    transform: rotate(-90deg) translate(-100%);
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-CommandPalette {
    display: flex;
    flex-direction: column;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    .lm-CommandPalette-search {
    flex: 0 0 auto;
    }

    .lm-CommandPalette-content {
    flex: 1 1 auto;
    margin: 0;
    padding: 0;
    min-height: 0;
    overflow: auto;
    list-style-type: none;
    }

    .lm-CommandPalette-header {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    }

    .lm-CommandPalette-item {
    display: flex;
    flex-direction: row;
    }

    .lm-CommandPalette-itemIcon {
    flex: 0 0 auto;
    }

    .lm-CommandPalette-itemContent {
    flex: 1 1 auto;
    overflow: hidden;
    }

    .lm-CommandPalette-itemShortcut {
    flex: 0 0 auto;
    }

    .lm-CommandPalette-itemLabel {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    }

    .lm-close-icon {
    border: 1px solid transparent;
    background-color: transparent;
    position: absolute;
    z-index: 1;
    right: 3%;
    top: 0;
    bottom: 0;
    margin: auto;
    padding: 7px 0;
    display: none;
    vertical-align: middle;
    outline: 0;
    cursor: pointer;
    }
    .lm-close-icon:after {
    content: 'X';
    display: block;
    width: 15px;
    height: 15px;
    text-align: center;
    color: #000;
    font-weight: normal;
    font-size: 12px;
    cursor: pointer;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-DockPanel {
    z-index: 0;
    }

    .lm-DockPanel-widget {
    z-index: 0;
    }

    .lm-DockPanel-tabBar {
    z-index: 1;
    }

    .lm-DockPanel-handle {
    z-index: 2;
    }

    .lm-DockPanel-handle.lm-mod-hidden {
    display: none !important;
    }

    .lm-DockPanel-handle:after {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    content: '';
    }

    .lm-DockPanel-handle[data-orientation='horizontal'] {
    cursor: ew-resize;
    }

    .lm-DockPanel-handle[data-orientation='vertical'] {
    cursor: ns-resize;
    }

    .lm-DockPanel-handle[data-orientation='horizontal']:after {
    left: 50%;
    min-width: 8px;
    transform: translateX(-50%);
    }

    .lm-DockPanel-handle[data-orientation='vertical']:after {
    top: 50%;
    min-height: 8px;
    transform: translateY(-50%);
    }

    .lm-DockPanel-overlay {
    z-index: 3;
    box-sizing: border-box;
    pointer-events: none;
    }

    .lm-DockPanel-overlay.lm-mod-hidden {
    display: none !important;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-Menu {
    z-index: 10000;
    position: absolute;
    white-space: nowrap;
    overflow-x: hidden;
    overflow-y: auto;
    outline: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    .lm-Menu-content {
    margin: 0;
    padding: 0;
    display: table;
    list-style-type: none;
    }

    .lm-Menu-item {
    display: table-row;
    }

    .lm-Menu-item.lm-mod-hidden,
    .lm-Menu-item.lm-mod-collapsed {
    display: none !important;
    }

    .lm-Menu-itemIcon,
    .lm-Menu-itemSubmenuIcon {
    display: table-cell;
    text-align: center;
    }

    .lm-Menu-itemLabel {
    display: table-cell;
    text-align: left;
    }

    .lm-Menu-itemShortcut {
    display: table-cell;
    text-align: right;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-MenuBar {
    outline: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    .lm-MenuBar-content {
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: row;
    list-style-type: none;
    }

    .lm-MenuBar-item {
    box-sizing: border-box;
    }

    .lm-MenuBar-itemIcon,
    .lm-MenuBar-itemLabel {
    display: inline-block;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-ScrollBar {
    display: flex;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    .lm-ScrollBar[data-orientation='horizontal'] {
    flex-direction: row;
    }

    .lm-ScrollBar[data-orientation='vertical'] {
    flex-direction: column;
    }

    .lm-ScrollBar-button {
    box-sizing: border-box;
    flex: 0 0 auto;
    }

    .lm-ScrollBar-track {
    box-sizing: border-box;
    position: relative;
    overflow: hidden;
    flex: 1 1 auto;
    }

    .lm-ScrollBar-thumb {
    box-sizing: border-box;
    position: absolute;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-SplitPanel-child {
    z-index: 0;
    }

    .lm-SplitPanel-handle {
    z-index: 1;
    }

    .lm-SplitPanel-handle.lm-mod-hidden {
    display: none !important;
    }

    .lm-SplitPanel-handle:after {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    content: '';
    }

    .lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
    cursor: ew-resize;
    }

    .lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
    cursor: ns-resize;
    }

    .lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
    left: 50%;
    min-width: 8px;
    transform: translateX(-50%);
    }

    .lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
    top: 50%;
    min-height: 8px;
    transform: translateY(-50%);
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-TabBar {
    display: flex;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    .lm-TabBar[data-orientation='horizontal'] {
    flex-direction: row;
    align-items: flex-end;
    }

    .lm-TabBar[data-orientation='vertical'] {
    flex-direction: column;
    align-items: flex-end;
    }

    .lm-TabBar-content {
    margin: 0;
    padding: 0;
    display: flex;
    flex: 1 1 auto;
    list-style-type: none;
    }

    .lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
    flex-direction: row;
    }

    .lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
    flex-direction: column;
    }

    .lm-TabBar-tab {
    display: flex;
    flex-direction: row;
    box-sizing: border-box;
    overflow: hidden;
    touch-action: none; /* Disable native Drag/Drop */
    }

    .lm-TabBar-tabIcon,
    .lm-TabBar-tabCloseIcon {
    flex: 0 0 auto;
    }

    .lm-TabBar-tabLabel {
    flex: 1 1 auto;
    overflow: hidden;
    white-space: nowrap;
    }

    .lm-TabBar-tabInput {
    user-select: all;
    width: 100%;
    box-sizing: border-box;
    }

    .lm-TabBar-tab.lm-mod-hidden {
    display: none !important;
    }

    .lm-TabBar-addButton.lm-mod-hidden {
    display: none !important;
    }

    .lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
    position: relative;
    }

    .lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
    left: 0;
    transition: left 150ms ease;
    }

    .lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
    top: 0;
    transition: top 150ms ease;
    }

    .lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
    transition: none;
    }

    .lm-TabBar-tabLabel .lm-TabBar-tabInput {
    user-select: all;
    width: 100%;
    box-sizing: border-box;
    background: inherit;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-TabPanel-tabBar {
    z-index: 1;
    }

    .lm-TabPanel-stackedPanel {
    z-index: 0;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-Collapse {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    }

    .jp-Collapse-header {
    padding: 1px 12px;
    background-color: var(--jp-layout-color1);
    border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
    color: var(--jp-ui-font-color1);
    cursor: pointer;
    display: flex;
    align-items: center;
    font-size: var(--jp-ui-font-size0);
    font-weight: 600;
    text-transform: uppercase;
    user-select: none;
    }

    .jp-Collapser-icon {
    height: 16px;
    }

    .jp-Collapse-header-collapsed .jp-Collapser-icon {
    transform: rotate(-90deg);
    margin: auto 0;
    }

    .jp-Collapser-title {
    line-height: 25px;
    }

    .jp-Collapse-contents {
    padding: 0 12px;
    background-color: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    overflow: auto;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

    /**
    * (DEPRECATED) Support for consuming icons as CSS background images
    */

    /* Icons urls */

    :root {
    --jp-icon-add-above: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5MikiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik00Ljc1IDQuOTMwNjZINi42MjVWNi44MDU2NkM2LjYyNSA3LjAxMTkxIDYuNzkzNzUgNy4xODA2NiA3IDcuMTgwNjZDNy4yMDYyNSA3LjE4MDY2IDcuMzc1IDcuMDExOTEgNy4zNzUgNi44MDU2NlY0LjkzMDY2SDkuMjVDOS40NTYyNSA0LjkzMDY2IDkuNjI1IDQuNzYxOTEgOS42MjUgNC41NTU2NkM5LjYyNSA0LjM0OTQxIDkuNDU2MjUgNC4xODA2NiA5LjI1IDQuMTgwNjZINy4zNzVWMi4zMDU2NkM3LjM3NSAyLjA5OTQxIDcuMjA2MjUgMS45MzA2NiA3IDEuOTMwNjZDNi43OTM3NSAxLjkzMDY2IDYuNjI1IDIuMDk5NDEgNi42MjUgMi4zMDU2NlY0LjE4MDY2SDQuNzVDNC41NDM3NSA0LjE4MDY2IDQuMzc1IDQuMzQ5NDEgNC4zNzUgNC41NTU2NkM0LjM3NSA0Ljc2MTkxIDQuNTQzNzUgNC45MzA2NiA0Ljc1IDQuOTMwNjZaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC43Ii8+CjwvZz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjUgOS41VjExLjVMMi41IDExLjVWOS41TDExLjUgOS41Wk0xMiA4QzEyLjU1MjMgOCAxMyA4LjQ0NzcyIDEzIDlWMTJDMTMgMTIuNTUyMyAxMi41NTIzIDEzIDEyIDEzTDIgMTNDMS40NDc3MiAxMyAxIDEyLjU1MjMgMSAxMlY5QzEgOC40NDc3MiAxLjQ0NzcxIDggMiA4TDEyIDhaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5MiI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDEwIDEuNTU1NjYpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==);
    --jp-icon-add-below: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5OCkiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik05LjI1IDEwLjA2OTNMNy4zNzUgMTAuMDY5M0w3LjM3NSA4LjE5NDM0QzcuMzc1IDcuOTg4MDkgNy4yMDYyNSA3LjgxOTM0IDcgNy44MTkzNEM2Ljc5Mzc1IDcuODE5MzQgNi42MjUgNy45ODgwOSA2LjYyNSA4LjE5NDM0TDYuNjI1IDEwLjA2OTNMNC43NSAxMC4wNjkzQzQuNTQzNzUgMTAuMDY5MyA0LjM3NSAxMC4yMzgxIDQuMzc1IDEwLjQ0NDNDNC4zNzUgMTAuNjUwNiA0LjU0Mzc1IDEwLjgxOTMgNC43NSAxMC44MTkzTDYuNjI1IDEwLjgxOTNMNi42MjUgMTIuNjk0M0M2LjYyNSAxMi45MDA2IDYuNzkzNzUgMTMuMDY5MyA3IDEzLjA2OTNDNy4yMDYyNSAxMy4wNjkzIDcuMzc1IDEyLjkwMDYgNy4zNzUgMTIuNjk0M0w3LjM3NSAxMC44MTkzTDkuMjUgMTAuODE5M0M5LjQ1NjI1IDEwLjgxOTMgOS42MjUgMTAuNjUwNiA5LjYyNSAxMC40NDQzQzkuNjI1IDEwLjIzODEgOS40NTYyNSAxMC4wNjkzIDkuMjUgMTAuMDY5M1oiIGZpbGw9IiM2MTYxNjEiIHN0cm9rZT0iIzYxNjE2MSIgc3Ryb2tlLXdpZHRoPSIwLjciLz4KPC9nPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDUuNUwyLjUgMy41TDExLjUgMy41TDExLjUgNS41TDIuNSA1LjVaTTIgN0MxLjQ0NzcyIDcgMSA2LjU1MjI4IDEgNkwxIDNDMSAyLjQ0NzcyIDEuNDQ3NzIgMiAyIDJMMTIgMkMxMi41NTIzIDIgMTMgMi40NDc3MiAxMyAzTDEzIDZDMTMgNi41NTIyOSAxMi41NTIzIDcgMTIgN0wyIDdaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5OCI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KDEgMS43NDg0NmUtMDcgMS43NDg0NmUtMDcgLTEgNCAxMy40NDQzKSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=);
    --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-bell: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiB2ZXJzaW9uPSIxLjEiPgogICA8cGF0aCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzMzMzMzIgogICAgICBkPSJtOCAwLjI5Yy0xLjQgMC0yLjcgMC43My0zLjYgMS44LTEuMiAxLjUtMS40IDMuNC0xLjUgNS4yLTAuMTggMi4yLTAuNDQgNC0yLjMgNS4zbDAuMjggMS4zaDVjMC4wMjYgMC42NiAwLjMyIDEuMSAwLjcxIDEuNSAwLjg0IDAuNjEgMiAwLjYxIDIuOCAwIDAuNTItMC40IDAuNi0xIDAuNzEtMS41aDVsMC4yOC0xLjNjLTEuOS0wLjk3LTIuMi0zLjMtMi4zLTUuMy0wLjEzLTEuOC0wLjI2LTMuNy0xLjUtNS4yLTAuODUtMS0yLjItMS44LTMuNi0xLjh6bTAgMS40YzAuODggMCAxLjkgMC41NSAyLjUgMS4zIDAuODggMS4xIDEuMSAyLjcgMS4yIDQuNCAwLjEzIDEuNyAwLjIzIDMuNiAxLjMgNS4yaC0xMGMxLjEtMS42IDEuMi0zLjQgMS4zLTUuMiAwLjEzLTEuNyAwLjMtMy4zIDEuMi00LjQgMC41OS0wLjcyIDEuNi0xLjMgMi41LTEuM3ptLTAuNzQgMTJoMS41Yy0wLjAwMTUgMC4yOCAwLjAxNSAwLjc5LTAuNzQgMC43OS0wLjczIDAuMDAxNi0wLjcyLTAuNTMtMC43NC0wLjc5eiIgLz4KPC9zdmc+Cg==);
    --jp-icon-bug-dot: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiPgogICAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTcuMTkgOEgyMFYxMEgxNy45MUMxNy45NiAxMC4zMyAxOCAxMC42NiAxOCAxMVYxMkgyMFYxNEgxOC41SDE4VjE0LjAyNzVDMTUuNzUgMTQuMjc2MiAxNCAxNi4xODM3IDE0IDE4LjVDMTQgMTkuMjA4IDE0LjE2MzUgMTkuODc3OSAxNC40NTQ5IDIwLjQ3MzlDMTMuNzA2MyAyMC44MTE3IDEyLjg3NTcgMjEgMTIgMjFDOS43OCAyMSA3Ljg1IDE5Ljc5IDYuODEgMThINFYxNkg2LjA5QzYuMDQgMTUuNjcgNiAxNS4zNCA2IDE1VjE0SDRWMTJINlYxMUM2IDEwLjY2IDYuMDQgMTAuMzMgNi4wOSAxMEg0VjhINi44MUM3LjI2IDcuMjIgNy44OCA2LjU1IDguNjIgNi4wNEw3IDQuNDFMOC40MSAzTDEwLjU5IDUuMTdDMTEuMDQgNS4wNiAxMS41MSA1IDEyIDVDMTIuNDkgNSAxMi45NiA1LjA2IDEzLjQyIDUuMTdMMTUuNTkgM0wxNyA0LjQxTDE1LjM3IDYuMDRDMTYuMTIgNi41NSAxNi43NCA3LjIyIDE3LjE5IDhaTTEwIDE2SDE0VjE0SDEwVjE2Wk0xMCAxMkgxNFYxMEgxMFYxMloiIGZpbGw9IiM2MTYxNjEiLz4KICAgICAgICA8cGF0aCBkPSJNMjIgMTguNUMyMiAyMC40MzMgMjAuNDMzIDIyIDE4LjUgMjJDMTYuNTY3IDIyIDE1IDIwLjQzMyAxNSAxOC41QzE1IDE2LjU2NyAxNi41NjcgMTUgMTguNSAxNUMyMC40MzMgMTUgMjIgMTYuNTY3IDIyIDE4LjVaIiBmaWxsPSIjNjE2MTYxIi8+CiAgICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
    --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
    --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-code-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CiAgICA8cGF0aCBkPSJNNi41OSwzLjQxTDIsOEw2LjU5LDEyLjZMOCwxMS4xOEw0LjgyLDhMOCw0LjgyTDYuNTksMy40MU0xMi40MSwzLjQxTDExLDQuODJMMTQuMTgsOEwxMSwxMS4xOEwxMi40MSwxMi42TDE3LDhMMTIuNDEsMy40MU0yMS41OSwxMS41OUwxMy41LDE5LjY4TDkuODMsMTZMOC40MiwxNy40MUwxMy41LDIyLjVMMjMsMTNMMjEuNTksMTEuNTlaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
    --jp-icon-collapse-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNNiAxM3YyaDh2LTJ6IiAvPgogICAgPC9nPgo8L3N2Zz4K);
    --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1jb25zb2xlLWljb24tYmFja2dyb3VuZC1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtY29uc29sZS1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIj4KICAgIDxwYXRoIGQ9Ik0xMDUgMTI3LjNoNDB2MTIuOGgtNDB6TTUxLjEgNzdMNzQgOTkuOWwtMjMuMyAyMy4zIDEwLjUgMTAuNSAyMy4zLTIzLjNMOTUgOTkuOSA4NC41IDg5LjQgNjEuNiA2Ni41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-delete: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCI+CiAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjI2MjYyIiBkPSJNNiAxOWMwIDEuMS45IDIgMiAyaDhjMS4xIDAgMi0uOSAyLTJWN0g2djEyek0xOSA0aC0zLjVsLTEtMWgtNWwtMSAxSDV2MmgxNFY0eiIgLz4KPC9zdmc+Cg==);
    --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-duplicate: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIuNzk5OTggMC44NzVIOC44OTU4MkM5LjIwMDYxIDAuODc1IDkuNDQ5OTggMS4xMzkxNCA5LjQ0OTk4IDEuNDYxOThDOS40NDk5OCAxLjc4NDgyIDkuMjAwNjEgMi4wNDg5NiA4Ljg5NTgyIDIuMDQ4OTZIMy4zNTQxNUMzLjA0OTM2IDIuMDQ4OTYgMi43OTk5OCAyLjMxMzEgMi43OTk5OCAyLjYzNTk0VjkuNjc5NjlDMi43OTk5OCAxMC4wMDI1IDIuNTUwNjEgMTAuMjY2NyAyLjI0NTgyIDEwLjI2NjdDMS45NDEwMyAxMC4yNjY3IDEuNjkxNjUgMTAuMDAyNSAxLjY5MTY1IDkuNjc5NjlWMi4wNDg5NkMxLjY5MTY1IDEuNDAzMjggMi4xOTA0IDAuODc1IDIuNzk5OTggMC44NzVaTTUuMzY2NjUgMTEuOVY0LjU1SDExLjA4MzNWMTEuOUg1LjM2NjY1Wk00LjE0MTY1IDQuMTQxNjdDNC4xNDE2NSAzLjY5MDYzIDQuNTA3MjggMy4zMjUgNC45NTgzMiAzLjMyNUgxMS40OTE3QzExLjk0MjcgMy4zMjUgMTIuMzA4MyAzLjY5MDYzIDEyLjMwODMgNC4xNDE2N1YxMi4zMDgzQzEyLjMwODMgMTIuNzU5NCAxMS45NDI3IDEzLjEyNSAxMS40OTE3IDEzLjEyNUg0Ljk1ODMyQzQuNTA3MjggMTMuMTI1IDQuMTQxNjUgMTIuNzU5NCA0LjE0MTY1IDEyLjMwODNWNC4xNDE2N1oiIGZpbGw9IiM2MTYxNjEiLz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNOS40MzU3NCA4LjI2NTA3SDguMzY0MzFWOS4zMzY1QzguMzY0MzEgOS40NTQzNSA4LjI2Nzg4IDkuNTUwNzggOC4xNTAwMiA5LjU1MDc4QzguMDMyMTcgOS41NTA3OCA3LjkzNTc0IDkuNDU0MzUgNy45MzU3NCA5LjMzNjVWOC4yNjUwN0g2Ljg2NDMxQzYuNzQ2NDUgOC4yNjUwNyA2LjY1MDAyIDguMTY4NjQgNi42NTAwMiA4LjA1MDc4QzYuNjUwMDIgNy45MzI5MiA2Ljc0NjQ1IDcuODM2NSA2Ljg2NDMxIDcuODM2NUg3LjkzNTc0VjYuNzY1MDdDNy45MzU3NCA2LjY0NzIxIDguMDMyMTcgNi41NTA3OCA4LjE1MDAyIDYuNTUwNzhDOC4yNjc4OCA2LjU1MDc4IDguMzY0MzEgNi42NDcyMSA4LjM2NDMxIDYuNzY1MDdWNy44MzY1SDkuNDM1NzRDOS41NTM2IDcuODM2NSA5LjY1MDAyIDcuOTMyOTIgOS42NTAwMiA4LjA1MDc4QzkuNjUwMDIgOC4xNjg2NCA5LjU1MzYgOC4yNjUwNyA5LjQzNTc0IDguMjY1MDdaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC41Ii8+Cjwvc3ZnPgo=);
    --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-error: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjE5IiByPSIyIi8+PHBhdGggZD0iTTEwIDNoNHYxMmgtNHoiLz48L2c+CjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiLz4KPC9zdmc+Cg==);
    --jp-icon-expand-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNMTEgMTBIOXYzSDZ2MmgzdjNoMnYtM2gzdi0yaC0zeiIgLz4KICAgIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
    --jp-icon-filter-dot: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWRvdCIgZmlsbD0iI0ZGRiI+CiAgICA8Y2lyY2xlIGN4PSIxOCIgY3k9IjE3IiByPSIzIj48L2NpcmNsZT4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-filter: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-folder-favorite: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6IiBmaWxsPSJub25lIi8+PHBhdGggY2xhc3M9ImpwLWljb24zIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxNjE2MSIgZD0iTTIwIDZoLThsLTItMkg0Yy0xLjEgMC0yIC45LTIgMnYxMmMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjhjMC0xLjEtLjktMi0yLTJ6bS0yLjA2IDExTDE1IDE1LjI4IDEyLjA2IDE3bC43OC0zLjMzLTIuNTktMi4yNCAzLjQxLS4yOUwxNSA4bDEuMzQgMy4xNCAzLjQxLjI5LTIuNTkgMi4yNC43OCAzLjMzeiIvPgo8L3N2Zz4K);
    --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
    --jp-icon-home: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xMCAyMHYtNmg0djZoNXYtOGgzTDEyIDMgMiAxMmgzdjh6Ii8+Cjwvc3ZnPgo=);
    --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
    --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
    --jp-icon-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUwLjk3OCA1MC45NzgiPgoJPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KCQk8cGF0aCBkPSJNNDMuNTIsNy40NThDMzguNzExLDIuNjQ4LDMyLjMwNywwLDI1LjQ4OSwwQzE4LjY3LDAsMTIuMjY2LDIuNjQ4LDcuNDU4LDcuNDU4CgkJCWMtOS45NDMsOS45NDEtOS45NDMsMjYuMTE5LDAsMzYuMDYyYzQuODA5LDQuODA5LDExLjIxMiw3LjQ1NiwxOC4wMzEsNy40NThjMCwwLDAuMDAxLDAsMC4wMDIsMAoJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoKCQkJIE00Mi4xMDYsNDIuMTA1Yy00LjQzMiw0LjQzMS0xMC4zMzIsNi44NzItMTYuNjE1LDYuODcyaC0wLjAwMmMtNi4yODUtMC4wMDEtMTIuMTg3LTIuNDQxLTE2LjYxNy02Ljg3MgoJCQljLTkuMTYyLTkuMTYzLTkuMTYyLTI0LjA3MSwwLTMzLjIzM0MxMy4zMDMsNC40NCwxOS4yMDQsMiwyNS40ODksMmM2LjI4NCwwLDEyLjE4NiwyLjQ0LDE2LjYxNyw2Ljg3MgoJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4KCQk8cGF0aCBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1MwoJCQljMC40NjgtMC41MzYsMC45MjMtMS4wNjIsMS4zNjctMS41NzVjMC42MjYtMC43NTMsMS4xMDQtMS40NzgsMS40MzYtMi4xNzVjMC4zMzEtMC43MDcsMC40OTUtMS41NDEsMC40OTUtMi41CgkJCWMwLTEuMDk2LTAuMjYtMi4wODgtMC43NzktMi45NzljLTAuNTY1LTAuODc5LTEuNTAxLTEuMzM2LTIuODA2LTEuMzY5Yy0xLjgwMiwwLjA1Ny0yLjk4NSwwLjY2Ny0zLjU1LDEuODMyCgkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkKCQkJYzEuMDYyLTEuNjQsMi44NTUtMi40ODEsNS4zNzgtMi41MjdjMi4xNiwwLjAyMywzLjg3NCwwLjYwOCw1LjE0MSwxLjc1OGMxLjI3OCwxLjE2LDEuOTI5LDIuNzY0LDEuOTUsNC44MTEKCQkJYzAsMS4xNDItMC4xMzcsMi4xMTEtMC40MSwyLjkxMWMtMC4zMDksMC44NDUtMC43MzEsMS41OTMtMS4yNjgsMi4yNDNjLTAuNDkyLDAuNjUtMS4wNjgsMS4zMTgtMS43MywyLjAwMgoJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5CgkJCUMyNi41ODksMzIuMjE4LDIzLjU3OCwzMi4yMTgsMjMuNTc4LDMyLjIxOHogTTIzLjU3OCwzOC4yMnYtMy40ODRoMy4wNzZ2My40ODRIMjMuNTc4eiIvPgoJPC9nPgo8L3N2Zz4K);
    --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaW5zcGVjdG9yLWljb24tY29sb3IganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
    --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtanNvbi1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0Y5QTgyNSI+CiAgICA8cGF0aCBkPSJNMjAuMiAxMS44Yy0xLjYgMC0xLjcuNS0xLjcgMSAwIC40LjEuOS4xIDEuMy4xLjUuMS45LjEgMS4zIDAgMS43LTEuNCAyLjMtMy41IDIuM2gtLjl2LTEuOWguNWMxLjEgMCAxLjQgMCAxLjQtLjggMC0uMyAwLS42LS4xLTEgMC0uNC0uMS0uOC0uMS0xLjIgMC0xLjMgMC0xLjggMS4zLTItMS4zLS4yLTEuMy0uNy0xLjMtMiAwLS40LjEtLjguMS0xLjIuMS0uNC4xLS43LjEtMSAwLS44LS40LS43LTEuNC0uOGgtLjVWNC4xaC45YzIuMiAwIDMuNS43IDMuNSAyLjMgMCAuNC0uMS45LS4xIDEuMy0uMS41LS4xLjktLjEgMS4zIDAgLjUuMiAxIDEuNyAxdjEuOHpNMS44IDEwLjFjMS42IDAgMS43LS41IDEuNy0xIDAtLjQtLjEtLjktLjEtMS4zLS4xLS41LS4xLS45LS4xLTEuMyAwLTEuNiAxLjQtMi4zIDMuNS0yLjNoLjl2MS45aC0uNWMtMSAwLTEuNCAwLTEuNC44IDAgLjMgMCAuNi4xIDEgMCAuMi4xLjYuMSAxIDAgMS4zIDAgMS44LTEuMyAyQzYgMTEuMiA2IDExLjcgNiAxM2MwIC40LS4xLjgtLjEgMS4yLS4xLjMtLjEuNy0uMSAxIDAgLjguMy44IDEuNC44aC41djEuOWgtLjljLTIuMSAwLTMuNS0uNi0zLjUtMi4zIDAtLjQuMS0uOS4xLTEuMy4xLS41LjEtLjkuMS0xLjMgMC0uNS0uMi0xLTEuNy0xdi0xLjl6Ii8+CiAgICA8Y2lyY2xlIGN4PSIxMSIgY3k9IjEzLjgiIHI9IjIuMSIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSI4LjIiIHI9IjIuMSIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgPGcgY2xhc3M9ImpwLWp1cHl0ZXItaWNvbi1jb2xvciIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgIDxnIGNsYXNzPSJqcC1qdXB5dGVyLWljb24tY29sb3IiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
    --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
    --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
    --jp-icon-launch: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIgMzIiIHdpZHRoPSIzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yNiwyOEg2YTIuMDAyNywyLjAwMjcsMCwwLDEtMi0yVjZBMi4wMDI3LDIuMDAyNywwLDAsMSw2LDRIMTZWNkg2VjI2SDI2VjE2aDJWMjZBMi4wMDI3LDIuMDAyNywwLDAsMSwyNiwyOFoiLz4KICAgIDxwb2x5Z29uIHBvaW50cz0iMjAgMiAyMCA0IDI2LjU4NiA0IDE4IDEyLjU4NiAxOS40MTQgMTQgMjggNS40MTQgMjggMTIgMzAgMTIgMzAgMiAyMCAyIi8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
    --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
    --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4K);
    --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
    --jp-icon-move-down: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMTIuNDcxIDcuNTI4OTlDMTIuNzYzMiA3LjIzNjg0IDEyLjc2MzIgNi43NjMxNiAxMi40NzEgNi40NzEwMVY2LjQ3MTAxQzEyLjE3OSA2LjE3OTA1IDExLjcwNTcgNi4xNzg4NCAxMS40MTM1IDYuNDcwNTRMNy43NSAxMC4xMjc1VjEuNzVDNy43NSAxLjMzNTc5IDcuNDE0MjEgMSA3IDFWMUM2LjU4NTc5IDEgNi4yNSAxLjMzNTc5IDYuMjUgMS43NVYxMC4xMjc1TDIuNTk3MjYgNi40NjgyMkMyLjMwMzM4IDYuMTczODEgMS44MjY0MSA2LjE3MzU5IDEuNTMyMjYgNi40Njc3NFY2LjQ2Nzc0QzEuMjM4MyA2Ljc2MTcgMS4yMzgzIDcuMjM4MyAxLjUzMjI2IDcuNTMyMjZMNi4yOTI4OSAxMi4yOTI5QzYuNjgzNDIgMTIuNjgzNCA3LjMxNjU4IDEyLjY4MzQgNy43MDcxMSAxMi4yOTI5TDEyLjQ3MSA3LjUyODk5WiIgZmlsbD0iIzYxNjE2MSIvPgo8L3N2Zz4K);
    --jp-icon-move-up: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMS41Mjg5OSA2LjQ3MTAxQzEuMjM2ODQgNi43NjMxNiAxLjIzNjg0IDcuMjM2ODQgMS41Mjg5OSA3LjUyODk5VjcuNTI4OTlDMS44MjA5NSA3LjgyMDk1IDIuMjk0MjYgNy44MjExNiAyLjU4NjQ5IDcuNTI5NDZMNi4yNSAzLjg3MjVWMTIuMjVDNi4yNSAxMi42NjQyIDYuNTg1NzkgMTMgNyAxM1YxM0M3LjQxNDIxIDEzIDcuNzUgMTIuNjY0MiA3Ljc1IDEyLjI1VjMuODcyNUwxMS40MDI3IDcuNTMxNzhDMTEuNjk2NiA3LjgyNjE5IDEyLjE3MzYgNy44MjY0MSAxMi40Njc3IDcuNTMyMjZWNy41MzIyNkMxMi43NjE3IDcuMjM4MyAxMi43NjE3IDYuNzYxNyAxMi40Njc3IDYuNDY3NzRMNy43MDcxMSAxLjcwNzExQzcuMzE2NTggMS4zMTY1OCA2LjY4MzQyIDEuMzE2NTggNi4yOTI4OSAxLjcwNzExTDEuNTI4OTkgNi40NzEwMVoiIGZpbGw9IiM2MTYxNjEiLz4KPC9zdmc+Cg==);
    --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
    --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtbm90ZWJvb2staWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
    --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
    --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iLTEwIC0xMCAxMzEuMTYxMzYxNjk0MzM1OTQgMTMyLjM4ODk5OTkzODk2NDg0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzA2OTk4IiBkPSJNIDU0LjkxODc4NSw5LjE5Mjc0MjFlLTQgQyA1MC4zMzUxMzIsMC4wMjIyMTcyNyA0NS45NTc4NDYsMC40MTMxMzY5NyA0Mi4xMDYyODUsMS4wOTQ2NjkzIDMwLjc2MDA2OSwzLjA5OTE3MzEgMjguNzAwMDM2LDcuMjk0NzcxNCAyOC43MDAwMzUsMTUuMDMyMTY5IHYgMTAuMjE4NzUgaCAyNi44MTI1IHYgMy40MDYyNSBoIC0yNi44MTI1IC0xMC4wNjI1IGMgLTcuNzkyNDU5LDAgLTE0LjYxNTc1ODgsNC42ODM3MTcgLTE2Ljc0OTk5OTgsMTMuNTkzNzUgLTIuNDYxODE5OTgsMTAuMjEyOTY2IC0yLjU3MTAxNTA4LDE2LjU4NjAyMyAwLDI3LjI1IDEuOTA1OTI4Myw3LjkzNzg1MiA2LjQ1NzU0MzIsMTMuNTkzNzQ4IDE0LjI0OTk5OTgsMTMuNTkzNzUgaCA5LjIxODc1IHYgLTEyLjI1IGMgMCwtOC44NDk5MDIgNy42NTcxNDQsLTE2LjY1NjI0OCAxNi43NSwtMTYuNjU2MjUgaCAyNi43ODEyNSBjIDcuNDU0OTUxLDAgMTMuNDA2MjUzLC02LjEzODE2NCAxMy40MDYyNSwtMTMuNjI1IHYgLTI1LjUzMTI1IGMgMCwtNy4yNjYzMzg2IC02LjEyOTk4LC0xMi43MjQ3NzcxIC0xMy40MDYyNSwtMTMuOTM3NDk5NyBDIDY0LjI4MTU0OCwwLjMyNzk0Mzk3IDU5LjUwMjQzOCwtMC4wMjAzNzkwMyA1NC45MTg3ODUsOS4xOTI3NDIxZS00IFogbSAtMTQuNSw4LjIxODc1MDEyNTc5IGMgMi43Njk1NDcsMCA1LjAzMTI1LDIuMjk4NjQ1NiA1LjAzMTI1LDUuMTI0OTk5NiAtMmUtNiwyLjgxNjMzNiAtMi4yNjE3MDMsNS4wOTM3NSAtNS4wMzEyNSw1LjA5Mzc1IC0yLjc3OTQ3NiwtMWUtNiAtNS4wMzEyNSwtMi4yNzc0MTUgLTUuMDMxMjUsLTUuMDkzNzUgLTEwZS03LC0yLjgyNjM1MyAyLjI1MTc3NCwtNS4xMjQ5OTk2IDUuMDMxMjUsLTUuMTI0OTk5NiB6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2ZmZDQzYiIgZD0ibSA4NS42Mzc1MzUsMjguNjU3MTY5IHYgMTEuOTA2MjUgYyAwLDkuMjMwNzU1IC03LjgyNTg5NSwxNi45OTk5OTkgLTE2Ljc1LDE3IGggLTI2Ljc4MTI1IGMgLTcuMzM1ODMzLDAgLTEzLjQwNjI0OSw2LjI3ODQ4MyAtMTMuNDA2MjUsMTMuNjI1IHYgMjUuNTMxMjQ3IGMgMCw3LjI2NjM0NCA2LjMxODU4OCwxMS41NDAzMjQgMTMuNDA2MjUsMTMuNjI1MDA0IDguNDg3MzMxLDIuNDk1NjEgMTYuNjI2MjM3LDIuOTQ2NjMgMjYuNzgxMjUsMCA2Ljc1MDE1NSwtMS45NTQzOSAxMy40MDYyNTMsLTUuODg3NjEgMTMuNDA2MjUsLTEzLjYyNTAwNCBWIDg2LjUwMDkxOSBoIC0yNi43ODEyNSB2IC0zLjQwNjI1IGggMjYuNzgxMjUgMTMuNDA2MjU0IGMgNy43OTI0NjEsMCAxMC42OTYyNTEsLTUuNDM1NDA4IDEzLjQwNjI0MSwtMTMuNTkzNzUgMi43OTkzMywtOC4zOTg4ODYgMi42ODAyMiwtMTYuNDc1Nzc2IDAsLTI3LjI1IC0xLjkyNTc4LC03Ljc1NzQ0MSAtNS42MDM4NywtMTMuNTkzNzUgLTEzLjQwNjI0MSwtMTMuNTkzNzUgeiBtIC0xNS4wNjI1LDY0LjY1NjI1IGMgMi43Nzk0NzgsM2UtNiA1LjAzMTI1LDIuMjc3NDE3IDUuMDMxMjUsNS4wOTM3NDcgLTJlLTYsMi44MjYzNTQgLTIuMjUxNzc1LDUuMTI1MDA0IC01LjAzMTI1LDUuMTI1MDA0IC0yLjc2OTU1LDAgLTUuMDMxMjUsLTIuMjk4NjUgLTUuMDMxMjUsLTUuMTI1MDA0IDJlLTYsLTIuODE2MzMgMi4yNjE2OTcsLTUuMDkzNzQ3IDUuMDMxMjUsLTUuMDkzNzQ3IHoiLz4KPC9zdmc+Cg==);
    --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
    --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
    --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
    --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
    --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
    --jp-icon-share: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTSAxOCAyIEMgMTYuMzU0OTkgMiAxNSAzLjM1NDk5MDQgMTUgNSBDIDE1IDUuMTkwOTUyOSAxNS4wMjE3OTEgNS4zNzcxMjI0IDE1LjA1NjY0MSA1LjU1ODU5MzggTCA3LjkyMTg3NSA5LjcyMDcwMzEgQyA3LjM5ODUzOTkgOS4yNzc4NTM5IDYuNzMyMDc3MSA5IDYgOSBDIDQuMzU0OTkwNCA5IDMgMTAuMzU0OTkgMyAxMiBDIDMgMTMuNjQ1MDEgNC4zNTQ5OTA0IDE1IDYgMTUgQyA2LjczMjA3NzEgMTUgNy4zOTg1Mzk5IDE0LjcyMjE0NiA3LjkyMTg3NSAxNC4yNzkyOTcgTCAxNS4wNTY2NDEgMTguNDM5NDUzIEMgMTUuMDIxNTU1IDE4LjYyMTUxNCAxNSAxOC44MDgzODYgMTUgMTkgQyAxNSAyMC42NDUwMSAxNi4zNTQ5OSAyMiAxOCAyMiBDIDE5LjY0NTAxIDIyIDIxIDIwLjY0NTAxIDIxIDE5IEMgMjEgMTcuMzU0OTkgMTkuNjQ1MDEgMTYgMTggMTYgQyAxNy4yNjc0OCAxNiAxNi42MDE1OTMgMTYuMjc5MzI4IDE2LjA3ODEyNSAxNi43MjI2NTYgTCA4Ljk0MzM1OTQgMTIuNTU4NTk0IEMgOC45NzgyMDk1IDEyLjM3NzEyMiA5IDEyLjE5MDk1MyA5IDEyIEMgOSAxMS44MDkwNDcgOC45NzgyMDk1IDExLjYyMjg3OCA4Ljk0MzM1OTQgMTEuNDQxNDA2IEwgMTYuMDc4MTI1IDcuMjc5Mjk2OSBDIDE2LjYwMTQ2IDcuNzIyMTQ2MSAxNy4yNjc5MjMgOCAxOCA4IEMgMTkuNjQ1MDEgOCAyMSA2LjY0NTAwOTYgMjEgNSBDIDIxIDMuMzU0OTkwNCAxOS42NDUwMSAyIDE4IDIgeiBNIDE4IDQgQyAxOC41NjQxMjkgNCAxOSA0LjQzNTg3MDYgMTkgNSBDIDE5IDUuNTY0MTI5NCAxOC41NjQxMjkgNiAxOCA2IEMgMTcuNDM1ODcxIDYgMTcgNS41NjQxMjk0IDE3IDUgQyAxNyA0LjQzNTg3MDYgMTcuNDM1ODcxIDQgMTggNCB6IE0gNiAxMSBDIDYuNTY0MTI5NCAxMSA3IDExLjQzNTg3MSA3IDEyIEMgNyAxMi41NjQxMjkgNi41NjQxMjk0IDEzIDYgMTMgQyA1LjQzNTg3MDYgMTMgNSAxMi41NjQxMjkgNSAxMiBDIDUgMTEuNDM1ODcxIDUuNDM1ODcwNiAxMSA2IDExIHogTSAxOCAxOCBDIDE4LjU2NDEyOSAxOCAxOSAxOC40MzU4NzEgMTkgMTkgQyAxOSAxOS41NjQxMjkgMTguNTY0MTI5IDIwIDE4IDIwIEMgMTcuNDM1ODcxIDIwIDE3IDE5LjU2NDEyOSAxNyAxOSBDIDE3IDE4LjQzNTg3MSAxNy40MzU4NzEgMTggMTggMTggeiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
    --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
    --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4K);
    --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
    --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1iYWNrZ3JvdW5kLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyIDIpIiBmaWxsPSIjMzMzMzMzIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUtaW52ZXJzZSIgZD0iTTUuMDU2NjQgOC43NjE3MkM1LjA1NjY0IDguNTk3NjYgNS4wMzEyNSA4LjQ1MzEyIDQuOTgwNDcgOC4zMjgxMkM0LjkzMzU5IDguMTk5MjIgNC44NTU0NyA4LjA4MjAzIDQuNzQ2MDkgNy45NzY1NkM0LjY0MDYyIDcuODcxMDkgNC41IDcuNzc1MzkgNC4zMjQyMiA3LjY4OTQ1QzQuMTUyMzQgNy41OTk2MSAzLjk0MzM2IDcuNTExNzIgMy42OTcyNyA3LjQyNTc4QzMuMzAyNzMgNy4yODUxNiAyLjk0MzM2IDcuMTM2NzIgMi42MTkxNCA2Ljk4MDQ3QzIuMjk0OTIgNi44MjQyMiAyLjAxNzU4IDYuNjQyNTggMS43ODcxMSA2LjQzNTU1QzEuNTYwNTUgNi4yMjg1MiAxLjM4NDc3IDUuOTg4MjggMS4yNTk3NyA1LjcxNDg0QzEuMTM0NzcgNS40Mzc1IDEuMDcyMjcgNS4xMDkzOCAxLjA3MjI3IDQuNzMwNDdDMS4wNzIyNyA0LjM5ODQ0IDEuMTI4OTEgNC4wOTU3IDEuMjQyMTkgMy44MjIyN0MxLjM1NTQ3IDMuNTQ0OTIgMS41MTU2MiAzLjMwNDY5IDEuNzIyNjYgMy4xMDE1NkMxLjkyOTY5IDIuODk4NDQgMi4xNzk2OSAyLjczNDM3IDIuNDcyNjYgMi42MDkzOEMyLjc2NTYyIDIuNDg0MzggMy4wOTE4IDIuNDA0MyAzLjQ1MTE3IDIuMzY5MTRWMS4xMDkzOEg0LjM4ODY3VjIuMzgwODZDNC43NDAyMyAyLjQyNzczIDUuMDU2NjQgMi41MjM0NCA1LjMzNzg5IDIuNjY3OTdDNS42MTkxNCAyLjgxMjUgNS44NTc0MiAzLjAwMTk1IDYuMDUyNzMgMy4yMzYzM0M2LjI1MTk1IDMuNDY2OCA2LjQwNDMgMy43NDAyMyA2LjUwOTc3IDQuMDU2NjRDNi42MTkxNCA0LjM2OTE0IDYuNjczODMgNC43MjA3IDYuNjczODMgNS4xMTEzM0g1LjA0NDkyQzUuMDQ0OTIgNC42Mzg2NyA0LjkzNzUgNC4yODEyNSA0LjcyMjY2IDQuMDM5MDZDNC41MDc4MSAzLjc5Mjk3IDQuMjE2OCAzLjY2OTkyIDMuODQ5NjEgMy42Njk5MkMzLjY1MDM5IDMuNjY5OTIgMy40NzY1NiAzLjY5NzI3IDMuMzI4MTIgMy43NTE5NUMzLjE4MzU5IDMuODAyNzMgMy4wNjQ0NSAzLjg3Njk1IDIuOTcwNyAzLjk3NDYxQzIuODc2OTUgNC4wNjgzNiAyLjgwNjY0IDQuMTc5NjkgMi43NTk3NyA0LjMwODU5QzIuNzE2OCA0LjQzNzUgMi42OTUzMSA0LjU3ODEyIDIuNjk1MzEgNC43MzA0N0MyLjY5NTMxIDQuODgyODEgMi43MTY4IDUuMDE5NTMgMi43NTk3NyA1LjE0MDYyQzIuODA2NjQgNS4yNTc4MSAyLjg4MjgxIDUuMzY3MTkgMi45ODgyOCA1LjQ2ODc1QzMuMDk3NjYgNS41NzAzMSAzLjI0MDIzIDUuNjY3OTcgMy40MTYwMiA1Ljc2MTcyQzMuNTkxOCA1Ljg1MTU2IDMuODEwNTUgNS45NDMzNiA0LjA3MjI3IDYuMDM3MTFDNC40NjY4IDYuMTg1NTUgNC44MjQyMiA2LjMzOTg0IDUuMTQ0NTMgNi41QzUuNDY0ODQgNi42NTYyNSA1LjczODI4IDYuODM5ODQgNS45NjQ4NCA3LjA1MDc4QzYuMTk1MzEgNy4yNTc4MSA2LjM3MTA5IDcuNSA2LjQ5MjE5IDcuNzc3MzRDNi42MTcxOSA4LjA1MDc4IDYuNjc5NjkgOC4zNzUgNi42Nzk2OSA4Ljc1QzYuNjc5NjkgOS4wOTM3NSA2LjYyMzA1IDkuNDA0MyA2LjUwOTc3IDkuNjgxNjRDNi4zOTY0OCA5Ljk1NTA4IDYuMjM0MzggMTAuMTkxNCA2LjAyMzQ0IDEwLjM5MDZDNS44MTI1IDEwLjU4OTggNS41NTg1OSAxMC43NSA1LjI2MTcyIDEwLjg3MTFDNC45NjQ4NCAxMC45ODgzIDQuNjMyODEgMTEuMDY0NSA0LjI2NTYyIDExLjA5OTZWMTIuMjQ4SDMuMzMzOThWMTEuMDk5NkMzLjAwMTk1IDExLjA2ODQgMi42Nzk2OSAxMC45OTYxIDIuMzY3MTkgMTAuODgyOEMyLjA1NDY5IDEwLjc2NTYgMS43NzczNCAxMC41OTc3IDEuNTM1MTYgMTAuMzc4OUMxLjI5Njg4IDEwLjE2MDIgMS4xMDU0NyA5Ljg4NDc3IDAuOTYwOTM4IDkuNTUyNzNDMC44MTY0MDYgOS4yMTY4IDAuNzQ0MTQxIDguODE0NDUgMC43NDQxNDEgOC4zNDU3SDIuMzc4OTFDMi4zNzg5MSA4LjYyNjk1IDIuNDE5OTIgOC44NjMyOCAyLjUwMTk1IDkuMDU0NjlDMi41ODM5OCA5LjI0MjE5IDIuNjg5NDUgOS4zOTI1OCAyLjgxODM2IDkuNTA1ODZDMi45NTExNyA5LjYxNTIzIDMuMTAxNTYgOS42OTMzNiAzLjI2OTUzIDkuNzQwMjNDMy40Mzc1IDkuNzg3MTEgMy42MDkzOCA5LjgxMDU1IDMuNzg1MTYgOS44MTA1NUM0LjIwMzEyIDkuODEwNTUgNC41MTk1MyA5LjcxMjg5IDQuNzM0MzggOS41MTc1OEM0Ljk0OTIyIDkuMzIyMjcgNS4wNTY2NCA5LjA3MDMxIDUuMDU2NjQgOC43NjE3MlpNMTMuNDE4IDEyLjI3MTVIOC4wNzQyMlYxMUgxMy40MThWMTIuMjcxNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuOTUyNjQgNikiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=);
    --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtdGV4dC1lZGl0b3ItaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xNSAxNUgzdjJoMTJ2LTJ6bTAtOEgzdjJoMTJWN3pNMyAxM2gxOHYtMkgzdjJ6bTAgOGgxOHYtMkgzdjJ6TTMgM3YyaDE4VjNIM3oiLz4KPC9zdmc+Cg==);
    --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4K);
    --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
    --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-user: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE2IDdhNCA0IDAgMTEtOCAwIDQgNCAwIDAxOCAwek0xMiAxNGE3IDcgMCAwMC03IDdoMTRhNyA3IDAgMDAtNy03eiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-users: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDM2IDI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGcgY2xhc3M9ImpwLWljb24zIiB0cmFuc2Zvcm09Im1hdHJpeCgxLjczMjcgMCAwIDEuNzMyNyAtMy42MjgyIC4wOTk1NzcpIiBmaWxsPSIjNjE2MTYxIj4KICA8cGF0aCB0cmFuc2Zvcm09Im1hdHJpeCgxLjUsMCwwLDEuNSwwLC02KSIgZD0ibTEyLjE4NiA3LjUwOThjLTEuMDUzNSAwLTEuOTc1NyAwLjU2NjUtMi40Nzg1IDEuNDEwMiAwLjc1MDYxIDAuMzEyNzcgMS4zOTc0IDAuODI2NDggMS44NzMgMS40NzI3aDMuNDg2M2MwLTEuNTkyLTEuMjg4OS0yLjg4MjgtMi44ODA5LTIuODgyOHoiLz4KICA8cGF0aCBkPSJtMjAuNDY1IDIuMzg5NWEyLjE4ODUgMi4xODg1IDAgMCAxLTIuMTg4NCAyLjE4ODUgMi4xODg1IDIuMTg4NSAwIDAgMS0yLjE4ODUtMi4xODg1IDIuMTg4NSAyLjE4ODUgMCAwIDEgMi4xODg1LTIuMTg4NSAyLjE4ODUgMi4xODg1IDAgMCAxIDIuMTg4NCAyLjE4ODV6Ii8+CiAgPHBhdGggdHJhbnNmb3JtPSJtYXRyaXgoMS41LDAsMCwxLjUsMCwtNikiIGQ9Im0zLjU4OTggOC40MjE5Yy0xLjExMjYgMC0yLjAxMzcgMC45MDExMS0yLjAxMzcgMi4wMTM3aDIuODE0NWMwLjI2Nzk3LTAuMzczMDkgMC41OTA3LTAuNzA0MzUgMC45NTg5OC0wLjk3ODUyLTAuMzQ0MzMtMC42MTY4OC0xLjAwMzEtMS4wMzUyLTEuNzU5OC0xLjAzNTJ6Ii8+CiAgPHBhdGggZD0ibTYuOTE1NCA0LjYyM2ExLjUyOTQgMS41Mjk0IDAgMCAxLTEuNTI5NCAxLjUyOTQgMS41Mjk0IDEuNTI5NCAwIDAgMS0xLjUyOTQtMS41Mjk0IDEuNTI5NCAxLjUyOTQgMCAwIDEgMS41Mjk0LTEuNTI5NCAxLjUyOTQgMS41Mjk0IDAgMCAxIDEuNTI5NCAxLjUyOTR6Ii8+CiAgPHBhdGggZD0ibTYuMTM1IDEzLjUzNWMwLTMuMjM5MiAyLjYyNTktNS44NjUgNS44NjUtNS44NjUgMy4yMzkyIDAgNS44NjUgMi42MjU5IDUuODY1IDUuODY1eiIvPgogIDxjaXJjbGUgY3g9IjEyIiBjeT0iMy43Njg1IiByPSIyLjk2ODUiLz4KIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-word: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KIDxnIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzQxNDE0MSI+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiA8L2c+CiA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguNDMgLjA0MDEpIiBmaWxsPSIjZmZmIj4KICA8cGF0aCBkPSJtNC4xNCA4Ljc2cTAuMDY4Mi0xLjg5IDIuNDItMS44OSAxLjE2IDAgMS42OCAwLjQyIDAuNTY3IDAuNDEgMC41NjcgMS4xNnYzLjQ3cTAgMC40NjIgMC41MTQgMC40NjIgMC4xMDMgMCAwLjItMC4wMjMxdjAuNzE0cS0wLjM5OSAwLjEwMy0wLjY1MSAwLjEwMy0wLjQ1MiAwLTAuNjkzLTAuMjItMC4yMzEtMC4yLTAuMjg0LTAuNjYyLTAuOTU2IDAuODcyLTIgMC44NzItMC45MDMgMC0xLjQ3LTAuNDcyLTAuNTI1LTAuNDcyLTAuNTI1LTEuMjYgMC0wLjI2MiAwLjA0NTItMC40NzIgMC4wNTY3LTAuMjIgMC4xMTYtMC4zNzggMC4wNjgyLTAuMTY4IDAuMjMxLTAuMzA0IDAuMTU4LTAuMTQ3IDAuMjYyLTAuMjQyIDAuMTE2LTAuMDkxNCAwLjM2OC0wLjE2OCAwLjI2Mi0wLjA5MTQgMC4zOTktMC4xMjYgMC4xMzYtMC4wNDUyIDAuNDcyLTAuMTAzIDAuMzM2LTAuMDU3OCAwLjUwNC0wLjA3OTggMC4xNTgtMC4wMjMxIDAuNTY3LTAuMDc5OCAwLjU1Ni0wLjA2ODIgMC43NzctMC4yMjEgMC4yMi0wLjE1MiAwLjIyLTAuNDQxdi0wLjI1MnEwLTAuNDMtMC4zNTctMC42NjItMC4zMzYtMC4yMzEtMC45NzYtMC4yMzEtMC42NjIgMC0wLjk5OCAwLjI2Mi0wLjMzNiAwLjI1Mi0wLjM5OSAwLjc5OHptMS44OSAzLjY4cTAuNzg4IDAgMS4yNi0wLjQxIDAuNTA0LTAuNDIgMC41MDQtMC45MDN2LTEuMDVxLTAuMjg0IDAuMTM2LTAuODYxIDAuMjMxLTAuNTY3IDAuMDkxNC0wLjk4NyAwLjE1OC0wLjQyIDAuMDY4Mi0wLjc2NiAwLjMyNi0wLjMzNiAwLjI1Mi0wLjMzNiAwLjcwNHQwLjMwNCAwLjcwNCAwLjg2MSAwLjI1MnoiIHN0cm9rZS13aWR0aD0iMS4wNSIvPgogIDxwYXRoIGQ9Im0xMCA0LjU2aDAuOTQ1djMuMTVxMC42NTEtMC45NzYgMS44OS0wLjk3NiAxLjE2IDAgMS44OSAwLjg0IDAuNjgyIDAuODQgMC42ODIgMi4zMSAwIDEuNDctMC43MDQgMi40Mi0wLjcwNCAwLjg4Mi0xLjg5IDAuODgyLTEuMjYgMC0xLjg5LTEuMDJ2MC43NjZoLTAuODV6bTIuNjIgMy4wNHEtMC43NDYgMC0xLjE2IDAuNjQtMC40NTIgMC42My0wLjQ1MiAxLjY4IDAgMS4wNSAwLjQ1MiAxLjY4dDEuMTYgMC42M3EwLjc3NyAwIDEuMjYtMC42MyAwLjQ5NC0wLjY0IDAuNDk0LTEuNjggMC0xLjA1LTAuNDcyLTEuNjgtMC40NjItMC42NC0xLjI2LTAuNjR6IiBzdHJva2Utd2lkdGg9IjEuMDUiLz4KICA8cGF0aCBkPSJtMi43MyAxNS44IDEzLjYgMC4wMDgxYzAuMDA2OSAwIDAtMi42IDAtMi42IDAtMC4wMDc4LTEuMTUgMC0xLjE1IDAtMC4wMDY5IDAtMC4wMDgzIDEuNS0wLjAwODMgMS41LTJlLTMgLTAuMDAxNC0xMS4zLTAuMDAxNC0xMS4zLTAuMDAxNGwtMC4wMDU5Mi0xLjVjMC0wLjAwNzgtMS4xNyAwLjAwMTMtMS4xNyAwLjAwMTN6IiBzdHJva2Utd2lkdGg9Ii45NzUiLz4KIDwvZz4KPC9zdmc+Cg==);
    --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
    }

    /* Icon CSS class declarations */

    .jp-AddAboveIcon {
    background-image: var(--jp-icon-add-above);
    }

    .jp-AddBelowIcon {
    background-image: var(--jp-icon-add-below);
    }

    .jp-AddIcon {
    background-image: var(--jp-icon-add);
    }

    .jp-BellIcon {
    background-image: var(--jp-icon-bell);
    }

    .jp-BugDotIcon {
    background-image: var(--jp-icon-bug-dot);
    }

    .jp-BugIcon {
    background-image: var(--jp-icon-bug);
    }

    .jp-BuildIcon {
    background-image: var(--jp-icon-build);
    }

    .jp-CaretDownEmptyIcon {
    background-image: var(--jp-icon-caret-down-empty);
    }

    .jp-CaretDownEmptyThinIcon {
    background-image: var(--jp-icon-caret-down-empty-thin);
    }

    .jp-CaretDownIcon {
    background-image: var(--jp-icon-caret-down);
    }

    .jp-CaretLeftIcon {
    background-image: var(--jp-icon-caret-left);
    }

    .jp-CaretRightIcon {
    background-image: var(--jp-icon-caret-right);
    }

    .jp-CaretUpEmptyThinIcon {
    background-image: var(--jp-icon-caret-up-empty-thin);
    }

    .jp-CaretUpIcon {
    background-image: var(--jp-icon-caret-up);
    }

    .jp-CaseSensitiveIcon {
    background-image: var(--jp-icon-case-sensitive);
    }

    .jp-CheckIcon {
    background-image: var(--jp-icon-check);
    }

    .jp-CircleEmptyIcon {
    background-image: var(--jp-icon-circle-empty);
    }

    .jp-CircleIcon {
    background-image: var(--jp-icon-circle);
    }

    .jp-ClearIcon {
    background-image: var(--jp-icon-clear);
    }

    .jp-CloseIcon {
    background-image: var(--jp-icon-close);
    }

    .jp-CodeCheckIcon {
    background-image: var(--jp-icon-code-check);
    }

    .jp-CodeIcon {
    background-image: var(--jp-icon-code);
    }

    .jp-CollapseAllIcon {
    background-image: var(--jp-icon-collapse-all);
    }

    .jp-ConsoleIcon {
    background-image: var(--jp-icon-console);
    }

    .jp-CopyIcon {
    background-image: var(--jp-icon-copy);
    }

    .jp-CopyrightIcon {
    background-image: var(--jp-icon-copyright);
    }

    .jp-CutIcon {
    background-image: var(--jp-icon-cut);
    }

    .jp-DeleteIcon {
    background-image: var(--jp-icon-delete);
    }

    .jp-DownloadIcon {
    background-image: var(--jp-icon-download);
    }

    .jp-DuplicateIcon {
    background-image: var(--jp-icon-duplicate);
    }

    .jp-EditIcon {
    background-image: var(--jp-icon-edit);
    }

    .jp-EllipsesIcon {
    background-image: var(--jp-icon-ellipses);
    }

    .jp-ErrorIcon {
    background-image: var(--jp-icon-error);
    }

    .jp-ExpandAllIcon {
    background-image: var(--jp-icon-expand-all);
    }

    .jp-ExtensionIcon {
    background-image: var(--jp-icon-extension);
    }

    .jp-FastForwardIcon {
    background-image: var(--jp-icon-fast-forward);
    }

    .jp-FileIcon {
    background-image: var(--jp-icon-file);
    }

    .jp-FileUploadIcon {
    background-image: var(--jp-icon-file-upload);
    }

    .jp-FilterDotIcon {
    background-image: var(--jp-icon-filter-dot);
    }

    .jp-FilterIcon {
    background-image: var(--jp-icon-filter);
    }

    .jp-FilterListIcon {
    background-image: var(--jp-icon-filter-list);
    }

    .jp-FolderFavoriteIcon {
    background-image: var(--jp-icon-folder-favorite);
    }

    .jp-FolderIcon {
    background-image: var(--jp-icon-folder);
    }

    .jp-HomeIcon {
    background-image: var(--jp-icon-home);
    }

    .jp-Html5Icon {
    background-image: var(--jp-icon-html5);
    }

    .jp-ImageIcon {
    background-image: var(--jp-icon-image);
    }

    .jp-InfoIcon {
    background-image: var(--jp-icon-info);
    }

    .jp-InspectorIcon {
    background-image: var(--jp-icon-inspector);
    }

    .jp-JsonIcon {
    background-image: var(--jp-icon-json);
    }

    .jp-JuliaIcon {
    background-image: var(--jp-icon-julia);
    }

    .jp-JupyterFaviconIcon {
    background-image: var(--jp-icon-jupyter-favicon);
    }

    .jp-JupyterIcon {
    background-image: var(--jp-icon-jupyter);
    }

    .jp-JupyterlabWordmarkIcon {
    background-image: var(--jp-icon-jupyterlab-wordmark);
    }

    .jp-KernelIcon {
    background-image: var(--jp-icon-kernel);
    }

    .jp-KeyboardIcon {
    background-image: var(--jp-icon-keyboard);
    }

    .jp-LaunchIcon {
    background-image: var(--jp-icon-launch);
    }

    .jp-LauncherIcon {
    background-image: var(--jp-icon-launcher);
    }

    .jp-LineFormIcon {
    background-image: var(--jp-icon-line-form);
    }

    .jp-LinkIcon {
    background-image: var(--jp-icon-link);
    }

    .jp-ListIcon {
    background-image: var(--jp-icon-list);
    }

    .jp-MarkdownIcon {
    background-image: var(--jp-icon-markdown);
    }

    .jp-MoveDownIcon {
    background-image: var(--jp-icon-move-down);
    }

    .jp-MoveUpIcon {
    background-image: var(--jp-icon-move-up);
    }

    .jp-NewFolderIcon {
    background-image: var(--jp-icon-new-folder);
    }

    .jp-NotTrustedIcon {
    background-image: var(--jp-icon-not-trusted);
    }

    .jp-NotebookIcon {
    background-image: var(--jp-icon-notebook);
    }

    .jp-NumberingIcon {
    background-image: var(--jp-icon-numbering);
    }

    .jp-OfflineBoltIcon {
    background-image: var(--jp-icon-offline-bolt);
    }

    .jp-PaletteIcon {
    background-image: var(--jp-icon-palette);
    }

    .jp-PasteIcon {
    background-image: var(--jp-icon-paste);
    }

    .jp-PdfIcon {
    background-image: var(--jp-icon-pdf);
    }

    .jp-PythonIcon {
    background-image: var(--jp-icon-python);
    }

    .jp-RKernelIcon {
    background-image: var(--jp-icon-r-kernel);
    }

    .jp-ReactIcon {
    background-image: var(--jp-icon-react);
    }

    .jp-RedoIcon {
    background-image: var(--jp-icon-redo);
    }

    .jp-RefreshIcon {
    background-image: var(--jp-icon-refresh);
    }

    .jp-RegexIcon {
    background-image: var(--jp-icon-regex);
    }

    .jp-RunIcon {
    background-image: var(--jp-icon-run);
    }

    .jp-RunningIcon {
    background-image: var(--jp-icon-running);
    }

    .jp-SaveIcon {
    background-image: var(--jp-icon-save);
    }

    .jp-SearchIcon {
    background-image: var(--jp-icon-search);
    }

    .jp-SettingsIcon {
    background-image: var(--jp-icon-settings);
    }

    .jp-ShareIcon {
    background-image: var(--jp-icon-share);
    }

    .jp-SpreadsheetIcon {
    background-image: var(--jp-icon-spreadsheet);
    }

    .jp-StopIcon {
    background-image: var(--jp-icon-stop);
    }

    .jp-TabIcon {
    background-image: var(--jp-icon-tab);
    }

    .jp-TableRowsIcon {
    background-image: var(--jp-icon-table-rows);
    }

    .jp-TagIcon {
    background-image: var(--jp-icon-tag);
    }

    .jp-TerminalIcon {
    background-image: var(--jp-icon-terminal);
    }

    .jp-TextEditorIcon {
    background-image: var(--jp-icon-text-editor);
    }

    .jp-TocIcon {
    background-image: var(--jp-icon-toc);
    }

    .jp-TreeViewIcon {
    background-image: var(--jp-icon-tree-view);
    }

    .jp-TrustedIcon {
    background-image: var(--jp-icon-trusted);
    }

    .jp-UndoIcon {
    background-image: var(--jp-icon-undo);
    }

    .jp-UserIcon {
    background-image: var(--jp-icon-user);
    }

    .jp-UsersIcon {
    background-image: var(--jp-icon-users);
    }

    .jp-VegaIcon {
    background-image: var(--jp-icon-vega);
    }

    .jp-WordIcon {
    background-image: var(--jp-icon-word);
    }

    .jp-YamlIcon {
    background-image: var(--jp-icon-yaml);
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /**
    * (DEPRECATED) Support for consuming icons as CSS background images
    */

    .jp-Icon,
    .jp-MaterialIcon {
    background-position: center;
    background-repeat: no-repeat;
    background-size: 16px;
    min-width: 16px;
    min-height: 16px;
    }

    .jp-Icon-cover {
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    }

    /**
    * (DEPRECATED) Support for specific CSS icon sizes
    */

    .jp-Icon-16 {
    background-size: 16px;
    min-width: 16px;
    min-height: 16px;
    }

    .jp-Icon-18 {
    background-size: 18px;
    min-width: 18px;
    min-height: 18px;
    }

    .jp-Icon-20 {
    background-size: 20px;
    min-width: 20px;
    min-height: 20px;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .lm-TabBar .lm-TabBar-addButton {
    align-items: center;
    display: flex;
    padding: 4px;
    padding-bottom: 5px;
    margin-right: 1px;
    background-color: var(--jp-layout-color2);
    }

    .lm-TabBar .lm-TabBar-addButton:hover {
    background-color: var(--jp-layout-color1);
    }

    .lm-DockPanel-tabBar .lm-TabBar-tab {
    width: var(--jp-private-horizontal-tab-width);
    }

    .lm-DockPanel-tabBar .lm-TabBar-content {
    flex: unset;
    }

    .lm-DockPanel-tabBar[data-orientation='horizontal'] {
    flex: 1 1 auto;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /**
    * Support for icons as inline SVG HTMLElements
    */

    /* recolor the primary elements of an icon */
    .jp-icon0[fill] {
    fill: var(--jp-inverse-layout-color0);
    }

    .jp-icon1[fill] {
    fill: var(--jp-inverse-layout-color1);
    }

    .jp-icon2[fill] {
    fill: var(--jp-inverse-layout-color2);
    }

    .jp-icon3[fill] {
    fill: var(--jp-inverse-layout-color3);
    }

    .jp-icon4[fill] {
    fill: var(--jp-inverse-layout-color4);
    }

    .jp-icon0[stroke] {
    stroke: var(--jp-inverse-layout-color0);
    }

    .jp-icon1[stroke] {
    stroke: var(--jp-inverse-layout-color1);
    }

    .jp-icon2[stroke] {
    stroke: var(--jp-inverse-layout-color2);
    }

    .jp-icon3[stroke] {
    stroke: var(--jp-inverse-layout-color3);
    }

    .jp-icon4[stroke] {
    stroke: var(--jp-inverse-layout-color4);
    }

    /* recolor the accent elements of an icon */
    .jp-icon-accent0[fill] {
    fill: var(--jp-layout-color0);
    }

    .jp-icon-accent1[fill] {
    fill: var(--jp-layout-color1);
    }

    .jp-icon-accent2[fill] {
    fill: var(--jp-layout-color2);
    }

    .jp-icon-accent3[fill] {
    fill: var(--jp-layout-color3);
    }

    .jp-icon-accent4[fill] {
    fill: var(--jp-layout-color4);
    }

    .jp-icon-accent0[stroke] {
    stroke: var(--jp-layout-color0);
    }

    .jp-icon-accent1[stroke] {
    stroke: var(--jp-layout-color1);
    }

    .jp-icon-accent2[stroke] {
    stroke: var(--jp-layout-color2);
    }

    .jp-icon-accent3[stroke] {
    stroke: var(--jp-layout-color3);
    }

    .jp-icon-accent4[stroke] {
    stroke: var(--jp-layout-color4);
    }

    /* set the color of an icon to transparent */
    .jp-icon-none[fill] {
    fill: none;
    }

    .jp-icon-none[stroke] {
    stroke: none;
    }

    /* brand icon colors. Same for light and dark */
    .jp-icon-brand0[fill] {
    fill: var(--jp-brand-color0);
    }

    .jp-icon-brand1[fill] {
    fill: var(--jp-brand-color1);
    }

    .jp-icon-brand2[fill] {
    fill: var(--jp-brand-color2);
    }

    .jp-icon-brand3[fill] {
    fill: var(--jp-brand-color3);
    }

    .jp-icon-brand4[fill] {
    fill: var(--jp-brand-color4);
    }

    .jp-icon-brand0[stroke] {
    stroke: var(--jp-brand-color0);
    }

    .jp-icon-brand1[stroke] {
    stroke: var(--jp-brand-color1);
    }

    .jp-icon-brand2[stroke] {
    stroke: var(--jp-brand-color2);
    }

    .jp-icon-brand3[stroke] {
    stroke: var(--jp-brand-color3);
    }

    .jp-icon-brand4[stroke] {
    stroke: var(--jp-brand-color4);
    }

    /* warn icon colors. Same for light and dark */
    .jp-icon-warn0[fill] {
    fill: var(--jp-warn-color0);
    }

    .jp-icon-warn1[fill] {
    fill: var(--jp-warn-color1);
    }

    .jp-icon-warn2[fill] {
    fill: var(--jp-warn-color2);
    }

    .jp-icon-warn3[fill] {
    fill: var(--jp-warn-color3);
    }

    .jp-icon-warn0[stroke] {
    stroke: var(--jp-warn-color0);
    }

    .jp-icon-warn1[stroke] {
    stroke: var(--jp-warn-color1);
    }

    .jp-icon-warn2[stroke] {
    stroke: var(--jp-warn-color2);
    }

    .jp-icon-warn3[stroke] {
    stroke: var(--jp-warn-color3);
    }

    /* icon colors that contrast well with each other and most backgrounds */
    .jp-icon-contrast0[fill] {
    fill: var(--jp-icon-contrast-color0);
    }

    .jp-icon-contrast1[fill] {
    fill: var(--jp-icon-contrast-color1);
    }

    .jp-icon-contrast2[fill] {
    fill: var(--jp-icon-contrast-color2);
    }

    .jp-icon-contrast3[fill] {
    fill: var(--jp-icon-contrast-color3);
    }

    .jp-icon-contrast0[stroke] {
    stroke: var(--jp-icon-contrast-color0);
    }

    .jp-icon-contrast1[stroke] {
    stroke: var(--jp-icon-contrast-color1);
    }

    .jp-icon-contrast2[stroke] {
    stroke: var(--jp-icon-contrast-color2);
    }

    .jp-icon-contrast3[stroke] {
    stroke: var(--jp-icon-contrast-color3);
    }

    .jp-icon-dot[fill] {
    fill: var(--jp-warn-color0);
    }

    .jp-jupyter-icon-color[fill] {
    fill: var(--jp-jupyter-icon-color, var(--jp-warn-color0));
    }

    .jp-notebook-icon-color[fill] {
    fill: var(--jp-notebook-icon-color, var(--jp-warn-color0));
    }

    .jp-json-icon-color[fill] {
    fill: var(--jp-json-icon-color, var(--jp-warn-color1));
    }

    .jp-console-icon-color[fill] {
    fill: var(--jp-console-icon-color, white);
    }

    .jp-console-icon-background-color[fill] {
    fill: var(--jp-console-icon-background-color, var(--jp-brand-color1));
    }

    .jp-terminal-icon-color[fill] {
    fill: var(--jp-terminal-icon-color, var(--jp-layout-color2));
    }

    .jp-terminal-icon-background-color[fill] {
    fill: var(
        --jp-terminal-icon-background-color,
        var(--jp-inverse-layout-color2)
    );
    }

    .jp-text-editor-icon-color[fill] {
    fill: var(--jp-text-editor-icon-color, var(--jp-inverse-layout-color3));
    }

    .jp-inspector-icon-color[fill] {
    fill: var(--jp-inspector-icon-color, var(--jp-inverse-layout-color3));
    }

    /* CSS for icons in selected filebrowser listing items */
    .jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
    fill: #fff;
    }

    .jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
    fill: var(--jp-brand-color1);
    }

    /* stylelint-disable selector-max-class, selector-max-compound-selectors */

    /**
    * TODO: come up with non css-hack solution for showing the busy icon on top
    *  of the close icon
    * CSS for complex behavior of close icon of tabs in the main area tabbar
    */
    .lm-DockPanel-tabBar
    .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
    > .lm-TabBar-tabCloseIcon
    > :not(:hover)
    > .jp-icon3[fill] {
    fill: none;
    }

    .lm-DockPanel-tabBar
    .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
    > .lm-TabBar-tabCloseIcon
    > :not(:hover)
    > .jp-icon-busy[fill] {
    fill: var(--jp-inverse-layout-color3);
    }

    /* stylelint-enable selector-max-class, selector-max-compound-selectors */

    /* CSS for icons in status bar */
    #jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
    fill: #fff;
    }

    #jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
    fill: var(--jp-brand-color1);
    }

    /* special handling for splash icon CSS. While the theme CSS reloads during
    splash, the splash icon can loose theming. To prevent that, we set a
    default for its color variable */
    :root {
    --jp-warn-color0: var(--md-orange-700);
    }

    /* not sure what to do with this one, used in filebrowser listing */
    .jp-DragIcon {
    margin-right: 4px;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /**
    * Support for alt colors for icons as inline SVG HTMLElements
    */

    /* alt recolor the primary elements of an icon */
    .jp-icon-alt .jp-icon0[fill] {
    fill: var(--jp-layout-color0);
    }

    .jp-icon-alt .jp-icon1[fill] {
    fill: var(--jp-layout-color1);
    }

    .jp-icon-alt .jp-icon2[fill] {
    fill: var(--jp-layout-color2);
    }

    .jp-icon-alt .jp-icon3[fill] {
    fill: var(--jp-layout-color3);
    }

    .jp-icon-alt .jp-icon4[fill] {
    fill: var(--jp-layout-color4);
    }

    .jp-icon-alt .jp-icon0[stroke] {
    stroke: var(--jp-layout-color0);
    }

    .jp-icon-alt .jp-icon1[stroke] {
    stroke: var(--jp-layout-color1);
    }

    .jp-icon-alt .jp-icon2[stroke] {
    stroke: var(--jp-layout-color2);
    }

    .jp-icon-alt .jp-icon3[stroke] {
    stroke: var(--jp-layout-color3);
    }

    .jp-icon-alt .jp-icon4[stroke] {
    stroke: var(--jp-layout-color4);
    }

    /* alt recolor the accent elements of an icon */
    .jp-icon-alt .jp-icon-accent0[fill] {
    fill: var(--jp-inverse-layout-color0);
    }

    .jp-icon-alt .jp-icon-accent1[fill] {
    fill: var(--jp-inverse-layout-color1);
    }

    .jp-icon-alt .jp-icon-accent2[fill] {
    fill: var(--jp-inverse-layout-color2);
    }

    .jp-icon-alt .jp-icon-accent3[fill] {
    fill: var(--jp-inverse-layout-color3);
    }

    .jp-icon-alt .jp-icon-accent4[fill] {
    fill: var(--jp-inverse-layout-color4);
    }

    .jp-icon-alt .jp-icon-accent0[stroke] {
    stroke: var(--jp-inverse-layout-color0);
    }

    .jp-icon-alt .jp-icon-accent1[stroke] {
    stroke: var(--jp-inverse-layout-color1);
    }

    .jp-icon-alt .jp-icon-accent2[stroke] {
    stroke: var(--jp-inverse-layout-color2);
    }

    .jp-icon-alt .jp-icon-accent3[stroke] {
    stroke: var(--jp-inverse-layout-color3);
    }

    .jp-icon-alt .jp-icon-accent4[stroke] {
    stroke: var(--jp-inverse-layout-color4);
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-icon-hoverShow:not(:hover) .jp-icon-hoverShow-content {
    display: none !important;
    }

    /**
    * Support for hover colors for icons as inline SVG HTMLElements
    */

    /**
    * regular colors
    */

    /* recolor the primary elements of an icon */
    .jp-icon-hover :hover .jp-icon0-hover[fill] {
    fill: var(--jp-inverse-layout-color0);
    }

    .jp-icon-hover :hover .jp-icon1-hover[fill] {
    fill: var(--jp-inverse-layout-color1);
    }

    .jp-icon-hover :hover .jp-icon2-hover[fill] {
    fill: var(--jp-inverse-layout-color2);
    }

    .jp-icon-hover :hover .jp-icon3-hover[fill] {
    fill: var(--jp-inverse-layout-color3);
    }

    .jp-icon-hover :hover .jp-icon4-hover[fill] {
    fill: var(--jp-inverse-layout-color4);
    }

    .jp-icon-hover :hover .jp-icon0-hover[stroke] {
    stroke: var(--jp-inverse-layout-color0);
    }

    .jp-icon-hover :hover .jp-icon1-hover[stroke] {
    stroke: var(--jp-inverse-layout-color1);
    }

    .jp-icon-hover :hover .jp-icon2-hover[stroke] {
    stroke: var(--jp-inverse-layout-color2);
    }

    .jp-icon-hover :hover .jp-icon3-hover[stroke] {
    stroke: var(--jp-inverse-layout-color3);
    }

    .jp-icon-hover :hover .jp-icon4-hover[stroke] {
    stroke: var(--jp-inverse-layout-color4);
    }

    /* recolor the accent elements of an icon */
    .jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
    fill: var(--jp-layout-color0);
    }

    .jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
    fill: var(--jp-layout-color1);
    }

    .jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
    fill: var(--jp-layout-color2);
    }

    .jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
    fill: var(--jp-layout-color3);
    }

    .jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
    fill: var(--jp-layout-color4);
    }

    .jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
    stroke: var(--jp-layout-color0);
    }

    .jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
    stroke: var(--jp-layout-color1);
    }

    .jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
    stroke: var(--jp-layout-color2);
    }

    .jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
    stroke: var(--jp-layout-color3);
    }

    .jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
    stroke: var(--jp-layout-color4);
    }

    /* set the color of an icon to transparent */
    .jp-icon-hover :hover .jp-icon-none-hover[fill] {
    fill: none;
    }

    .jp-icon-hover :hover .jp-icon-none-hover[stroke] {
    stroke: none;
    }

    /**
    * inverse colors
    */

    /* inverse recolor the primary elements of an icon */
    .jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
    fill: var(--jp-layout-color0);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
    fill: var(--jp-layout-color1);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
    fill: var(--jp-layout-color2);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
    fill: var(--jp-layout-color3);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
    fill: var(--jp-layout-color4);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
    stroke: var(--jp-layout-color0);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
    stroke: var(--jp-layout-color1);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
    stroke: var(--jp-layout-color2);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
    stroke: var(--jp-layout-color3);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
    stroke: var(--jp-layout-color4);
    }

    /* inverse recolor the accent elements of an icon */
    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
    fill: var(--jp-inverse-layout-color0);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
    fill: var(--jp-inverse-layout-color1);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
    fill: var(--jp-inverse-layout-color2);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
    fill: var(--jp-inverse-layout-color3);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
    fill: var(--jp-inverse-layout-color4);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
    stroke: var(--jp-inverse-layout-color0);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
    stroke: var(--jp-inverse-layout-color1);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
    stroke: var(--jp-inverse-layout-color2);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
    stroke: var(--jp-inverse-layout-color3);
    }

    .jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
    stroke: var(--jp-inverse-layout-color4);
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-IFrame {
    width: 100%;
    height: 100%;
    }

    .jp-IFrame > iframe {
    border: none;
    }

    /*
    When drag events occur, `lm-mod-override-cursor` is added to the body.
    Because iframes steal all cursor events, the following two rules are necessary
    to suppress pointer events while resize drags are occurring. There may be a
    better solution to this problem.
    */
    body.lm-mod-override-cursor .jp-IFrame {
    position: relative;
    }

    body.lm-mod-override-cursor .jp-IFrame::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: transparent;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) 2014-2016, Jupyter Development Team.
    |
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-HoverBox {
    position: fixed;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-FormGroup-content fieldset {
    border: none;
    padding: 0;
    min-width: 0;
    width: 100%;
    }

    /* stylelint-disable selector-max-type */

    .jp-FormGroup-content fieldset .jp-inputFieldWrapper input,
    .jp-FormGroup-content fieldset .jp-inputFieldWrapper select,
    .jp-FormGroup-content fieldset .jp-inputFieldWrapper textarea {
    font-size: var(--jp-content-font-size2);
    border-color: var(--jp-input-border-color);
    border-style: solid;
    border-radius: var(--jp-border-radius);
    border-width: 1px;
    padding: 6px 8px;
    background: none;
    color: var(--jp-ui-font-color0);
    height: inherit;
    }

    .jp-FormGroup-content fieldset input[type='checkbox'] {
    position: relative;
    top: 2px;
    margin-left: 0;
    }

    .jp-FormGroup-content button.jp-mod-styled {
    cursor: pointer;
    }

    .jp-FormGroup-content .checkbox label {
    cursor: pointer;
    font-size: var(--jp-content-font-size1);
    }

    .jp-FormGroup-content .jp-root > fieldset > legend {
    display: none;
    }

    .jp-FormGroup-content .jp-root > fieldset > p {
    display: none;
    }

    /** copy of `input.jp-mod-styled:focus` style */
    .jp-FormGroup-content fieldset input:focus,
    .jp-FormGroup-content fieldset select:focus {
    -moz-outline-radius: unset;
    outline: var(--jp-border-width) solid var(--md-blue-500);
    outline-offset: -1px;
    box-shadow: inset 0 0 4px var(--md-blue-300);
    }

    .jp-FormGroup-content fieldset input:hover:not(:focus),
    .jp-FormGroup-content fieldset select:hover:not(:focus) {
    background-color: var(--jp-border-color2);
    }

    /* stylelint-enable selector-max-type */

    .jp-FormGroup-content .checkbox .field-description {
    /* Disable default description field for checkbox:
    because other widgets do not have description fields,
    we add descriptions to each widget on the field level.
    */
    display: none;
    }

    .jp-FormGroup-content #root__description {
    display: none;
    }

    .jp-FormGroup-content .jp-modifiedIndicator {
    width: 5px;
    background-color: var(--jp-brand-color2);
    margin-top: 0;
    margin-left: calc(var(--jp-private-settingeditor-modifier-indent) * -1);
    flex-shrink: 0;
    }

    .jp-FormGroup-content .jp-modifiedIndicator.jp-errorIndicator {
    background-color: var(--jp-error-color0);
    margin-right: 0.5em;
    }

    /* RJSF ARRAY style */

    .jp-arrayFieldWrapper legend {
    font-size: var(--jp-content-font-size2);
    color: var(--jp-ui-font-color0);
    flex-basis: 100%;
    padding: 4px 0;
    font-weight: var(--jp-content-heading-font-weight);
    border-bottom: 1px solid var(--jp-border-color2);
    }

    .jp-arrayFieldWrapper .field-description {
    padding: 4px 0;
    white-space: pre-wrap;
    }

    .jp-arrayFieldWrapper .array-item {
    width: 100%;
    border: 1px solid var(--jp-border-color2);
    border-radius: 4px;
    margin: 4px;
    }

    .jp-ArrayOperations {
    display: flex;
    margin-left: 8px;
    }

    .jp-ArrayOperationsButton {
    margin: 2px;
    }

    .jp-ArrayOperationsButton .jp-icon3[fill] {
    fill: var(--jp-ui-font-color0);
    }

    button.jp-ArrayOperationsButton.jp-mod-styled:disabled {
    cursor: not-allowed;
    opacity: 0.5;
    }

    /* RJSF form validation error */

    .jp-FormGroup-content .validationErrors {
    color: var(--jp-error-color0);
    }

    /* Hide panel level error as duplicated the field level error */
    .jp-FormGroup-content .panel.errors {
    display: none;
    }

    /* RJSF normal content (settings-editor) */

    .jp-FormGroup-contentNormal {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    }

    .jp-FormGroup-contentNormal .jp-FormGroup-contentItem {
    margin-left: 7px;
    color: var(--jp-ui-font-color0);
    }

    .jp-FormGroup-contentNormal .jp-FormGroup-description {
    flex-basis: 100%;
    padding: 4px 7px;
    }

    .jp-FormGroup-contentNormal .jp-FormGroup-default {
    flex-basis: 100%;
    padding: 4px 7px;
    }

    .jp-FormGroup-contentNormal .jp-FormGroup-fieldLabel {
    font-size: var(--jp-content-font-size1);
    font-weight: normal;
    min-width: 120px;
    }

    .jp-FormGroup-contentNormal fieldset:not(:first-child) {
    margin-left: 7px;
    }

    .jp-FormGroup-contentNormal .field-array-of-string .array-item {
    /* Display `jp-ArrayOperations` buttons side-by-side with content except
        for small screens where flex-wrap will place them one below the other.
    */
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    }

    .jp-FormGroup-contentNormal .jp-objectFieldWrapper .form-group {
    padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
    margin-top: 2px;
    }

    /* RJSF compact content (metadata-form) */

    .jp-FormGroup-content.jp-FormGroup-contentCompact {
    width: 100%;
    }

    .jp-FormGroup-contentCompact .form-group {
    display: flex;
    padding: 0.5em 0.2em 0.5em 0;
    }

    .jp-FormGroup-contentCompact
    .jp-FormGroup-compactTitle
    .jp-FormGroup-description {
    font-size: var(--jp-ui-font-size1);
    color: var(--jp-ui-font-color2);
    }

    .jp-FormGroup-contentCompact .jp-FormGroup-fieldLabel {
    padding-bottom: 0.3em;
    }

    .jp-FormGroup-contentCompact .jp-inputFieldWrapper .form-control {
    width: 100%;
    box-sizing: border-box;
    }

    .jp-FormGroup-contentCompact .jp-arrayFieldWrapper .jp-FormGroup-compactTitle {
    padding-bottom: 7px;
    }

    .jp-FormGroup-contentCompact
    .jp-objectFieldWrapper
    .jp-objectFieldWrapper
    .form-group {
    padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
    margin-top: 2px;
    }

    .jp-FormGroup-contentCompact ul.error-detail {
    margin-block-start: 0.5em;
    margin-block-end: 0.5em;
    padding-inline-start: 1em;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    .jp-SidePanel {
    display: flex;
    flex-direction: column;
    min-width: var(--jp-sidebar-min-width);
    overflow-y: auto;
    color: var(--jp-ui-font-color1);
    background: var(--jp-layout-color1);
    font-size: var(--jp-ui-font-size1);
    }

    .jp-SidePanel-header {
    flex: 0 0 auto;
    display: flex;
    border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
    font-size: var(--jp-ui-font-size0);
    font-weight: 600;
    letter-spacing: 1px;
    margin: 0;
    padding: 2px;
    text-transform: uppercase;
    }

    .jp-SidePanel-toolbar {
    flex: 0 0 auto;
    }

    .jp-SidePanel-content {
    flex: 1 1 auto;
    }

    .jp-SidePanel-toolbar,
    .jp-AccordionPanel-toolbar {
    height: var(--jp-private-toolbar-height);
    }

    .jp-SidePanel-toolbar.jp-Toolbar-micro {
    display: none;
    }

    .lm-AccordionPanel .jp-AccordionPanel-title {
    box-sizing: border-box;
    line-height: 25px;
    margin: 0;
    display: flex;
    align-items: center;
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
    box-shadow: var(--jp-toolbar-box-shadow);
    font-size: var(--jp-ui-font-size0);
    }

    .jp-AccordionPanel-title {
    cursor: pointer;
    user-select: none;
    -moz-user-select: none;
    -webkit-user-select: none;
    text-transform: uppercase;
    }

    .lm-AccordionPanel[data-orientation='horizontal'] > .jp-AccordionPanel-title {
    /* Title is rotated for horizontal accordion panel using CSS */
    display: block;
    transform-origin: top left;
    transform: rotate(-90deg) translate(-100%);
    }

    .jp-AccordionPanel-title .lm-AccordionPanel-titleLabel {
    user-select: none;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
    }

    .jp-AccordionPanel-title .lm-AccordionPanel-titleCollapser {
    transform: rotate(-90deg);
    margin: auto 0;
    height: 16px;
    }

    .jp-AccordionPanel-title.lm-mod-expanded .lm-AccordionPanel-titleCollapser {
    transform: rotate(0deg);
    }

    .lm-AccordionPanel .jp-AccordionPanel-toolbar {
    background: none;
    box-shadow: none;
    border: none;
    margin-left: auto;
    }

    .lm-AccordionPanel .lm-SplitPanel-handle:hover {
    background: var(--jp-layout-color3);
    }

    .jp-text-truncated {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) 2017, Jupyter Development Team.
    |
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-Spinner {
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 10;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: var(--jp-layout-color0);
    outline: none;
    }

    .jp-SpinnerContent {
    font-size: 10px;
    margin: 50px auto;
    text-indent: -9999em;
    width: 3em;
    height: 3em;
    border-radius: 50%;
    background: var(--jp-brand-color3);
    background: linear-gradient(
        to right,
        #f37626 10%,
        rgba(255, 255, 255, 0) 42%
    );
    position: relative;
    animation: load3 1s infinite linear, fadeIn 1s;
    }

    .jp-SpinnerContent::before {
    width: 50%;
    height: 50%;
    background: #f37626;
    border-radius: 100% 0 0;
    position: absolute;
    top: 0;
    left: 0;
    content: '';
    }

    .jp-SpinnerContent::after {
    background: var(--jp-layout-color0);
    width: 75%;
    height: 75%;
    border-radius: 50%;
    content: '';
    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    }

    @keyframes fadeIn {
    0% {
        opacity: 0;
    }

    100% {
        opacity: 1;
    }
    }

    @keyframes load3 {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) 2014-2017, Jupyter Development Team.
    |
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    button.jp-mod-styled {
    font-size: var(--jp-ui-font-size1);
    color: var(--jp-ui-font-color0);
    border: none;
    box-sizing: border-box;
    text-align: center;
    line-height: 32px;
    height: 32px;
    padding: 0 12px;
    letter-spacing: 0.8px;
    outline: none;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    }

    input.jp-mod-styled {
    background: var(--jp-input-background);
    height: 28px;
    box-sizing: border-box;
    border: var(--jp-border-width) solid var(--jp-border-color1);
    padding-left: 7px;
    padding-right: 7px;
    font-size: var(--jp-ui-font-size2);
    color: var(--jp-ui-font-color0);
    outline: none;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    }

    input[type='checkbox'].jp-mod-styled {
    appearance: checkbox;
    -webkit-appearance: checkbox;
    -moz-appearance: checkbox;
    height: auto;
    }

    input.jp-mod-styled:focus {
    border: var(--jp-border-width) solid var(--md-blue-500);
    box-shadow: inset 0 0 4px var(--md-blue-300);
    }

    .jp-select-wrapper {
    display: flex;
    position: relative;
    flex-direction: column;
    padding: 1px;
    background-color: var(--jp-layout-color1);
    box-sizing: border-box;
    margin-bottom: 12px;
    }

    .jp-select-wrapper:not(.multiple) {
    height: 28px;
    }

    .jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
    border: var(--jp-border-width) solid var(--jp-input-active-border-color);
    box-shadow: var(--jp-input-box-shadow);
    background-color: var(--jp-input-active-background);
    }

    select.jp-mod-styled:hover {
    cursor: pointer;
    color: var(--jp-ui-font-color0);
    background-color: var(--jp-input-hover-background);
    box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.5);
    }

    select.jp-mod-styled {
    flex: 1 1 auto;
    width: 100%;
    font-size: var(--jp-ui-font-size2);
    background: var(--jp-input-background);
    color: var(--jp-ui-font-color0);
    padding: 0 25px 0 8px;
    border: var(--jp-border-width) solid var(--jp-input-border-color);
    border-radius: 0;
    outline: none;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    }

    select.jp-mod-styled:not([multiple]) {
    height: 32px;
    }

    select.jp-mod-styled[multiple] {
    max-height: 200px;
    overflow-y: auto;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-switch {
    display: flex;
    align-items: center;
    padding-left: 4px;
    padding-right: 4px;
    font-size: var(--jp-ui-font-size1);
    background-color: transparent;
    color: var(--jp-ui-font-color1);
    border: none;
    height: 20px;
    }

    .jp-switch:hover {
    background-color: var(--jp-layout-color2);
    }

    .jp-switch-label {
    margin-right: 5px;
    font-family: var(--jp-ui-font-family);
    }

    .jp-switch-track {
    cursor: pointer;
    background-color: var(--jp-switch-color, var(--jp-border-color1));
    -webkit-transition: 0.4s;
    transition: 0.4s;
    border-radius: 34px;
    height: 16px;
    width: 35px;
    position: relative;
    }

    .jp-switch-track::before {
    content: '';
    position: absolute;
    height: 10px;
    width: 10px;
    margin: 3px;
    left: 0;
    background-color: var(--jp-ui-inverse-font-color1);
    -webkit-transition: 0.4s;
    transition: 0.4s;
    border-radius: 50%;
    }

    .jp-switch[aria-checked='true'] .jp-switch-track {
    background-color: var(--jp-switch-true-position-color, var(--jp-warn-color0));
    }

    .jp-switch[aria-checked='true'] .jp-switch-track::before {
    /* track width (35) - margins (3 + 3) - thumb width (10) */
    left: 19px;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) 2014-2016, Jupyter Development Team.
    |
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    :root {
    --jp-private-toolbar-height: calc(
        28px + var(--jp-border-width)
    ); /* leave 28px for content */
    }

    .jp-Toolbar {
    color: var(--jp-ui-font-color1);
    flex: 0 0 auto;
    display: flex;
    flex-direction: row;
    border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
    box-shadow: var(--jp-toolbar-box-shadow);
    background: var(--jp-toolbar-background);
    min-height: var(--jp-toolbar-micro-height);
    padding: 2px;
    z-index: 8;
    overflow-x: hidden;
    }

    /* Toolbar items */

    .jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
    flex-grow: 1;
    flex-shrink: 1;
    }

    .jp-Toolbar-item.jp-Toolbar-kernelStatus {
    display: inline-block;
    width: 32px;
    background-repeat: no-repeat;
    background-position: center;
    background-size: 16px;
    }

    .jp-Toolbar > .jp-Toolbar-item {
    flex: 0 0 auto;
    display: flex;
    padding-left: 1px;
    padding-right: 1px;
    font-size: var(--jp-ui-font-size1);
    line-height: var(--jp-private-toolbar-height);
    height: 100%;
    }

    /* Toolbar buttons */

    /* This is the div we use to wrap the react component into a Widget */
    div.jp-ToolbarButton {
    color: transparent;
    border: none;
    box-sizing: border-box;
    outline: none;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    padding: 0;
    margin: 0;
    }

    button.jp-ToolbarButtonComponent {
    background: var(--jp-layout-color1);
    border: none;
    box-sizing: border-box;
    outline: none;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    padding: 0 6px;
    margin: 0;
    height: 24px;
    border-radius: var(--jp-border-radius);
    display: flex;
    align-items: center;
    text-align: center;
    font-size: 14px;
    min-width: unset;
    min-height: unset;
    }

    button.jp-ToolbarButtonComponent:disabled {
    opacity: 0.4;
    }

    button.jp-ToolbarButtonComponent > span {
    padding: 0;
    flex: 0 0 auto;
    }

    button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
    font-size: var(--jp-ui-font-size1);
    line-height: 100%;
    padding-left: 2px;
    color: var(--jp-ui-font-color1);
    font-family: var(--jp-ui-font-family);
    }

    #jp-main-dock-panel[data-mode='single-document']
    .jp-MainAreaWidget
    > .jp-Toolbar.jp-Toolbar-micro {
    padding: 0;
    min-height: 0;
    }

    #jp-main-dock-panel[data-mode='single-document']
    .jp-MainAreaWidget
    > .jp-Toolbar {
    border: none;
    box-shadow: none;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    .jp-WindowedPanel-outer {
    position: relative;
    overflow-y: auto;
    }

    .jp-WindowedPanel-inner {
    position: relative;
    }

    .jp-WindowedPanel-window {
    position: absolute;
    left: 0;
    right: 0;
    overflow: visible;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /* Sibling imports */

    body {
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    }

    /* Disable native link decoration styles everywhere outside of dialog boxes */
    a {
    text-decoration: unset;
    color: unset;
    }

    a:hover {
    text-decoration: unset;
    color: unset;
    }

    /* Accessibility for links inside dialog box text */
    .jp-Dialog-content a {
    text-decoration: revert;
    color: var(--jp-content-link-color);
    }

    .jp-Dialog-content a:hover {
    text-decoration: revert;
    }

    /* Styles for ui-components */
    .jp-Button {
    color: var(--jp-ui-font-color2);
    border-radius: var(--jp-border-radius);
    padding: 0 12px;
    font-size: var(--jp-ui-font-size1);

    /* Copy from blueprint 3 */
    display: inline-flex;
    flex-direction: row;
    border: none;
    cursor: pointer;
    align-items: center;
    justify-content: center;
    text-align: left;
    vertical-align: middle;
    min-height: 30px;
    min-width: 30px;
    }

    .jp-Button:disabled {
    cursor: not-allowed;
    }

    .jp-Button:empty {
    padding: 0 !important;
    }

    .jp-Button.jp-mod-small {
    min-height: 24px;
    min-width: 24px;
    font-size: 12px;
    padding: 0 7px;
    }

    /* Use our own theme for hover styles */
    .jp-Button.jp-mod-minimal:hover {
    background-color: var(--jp-layout-color2);
    }

    .jp-Button.jp-mod-minimal {
    background: none;
    }

    .jp-InputGroup {
    display: block;
    position: relative;
    }

    .jp-InputGroup input {
    box-sizing: border-box;
    border: none;
    border-radius: 0;
    background-color: transparent;
    color: var(--jp-ui-font-color0);
    box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
    padding-bottom: 0;
    padding-top: 0;
    padding-left: 10px;
    padding-right: 28px;
    position: relative;
    width: 100%;
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    font-size: 14px;
    font-weight: 400;
    height: 30px;
    line-height: 30px;
    outline: none;
    vertical-align: middle;
    }

    .jp-InputGroup input:focus {
    box-shadow: inset 0 0 0 var(--jp-border-width)
        var(--jp-input-active-box-shadow-color),
        inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
    }

    .jp-InputGroup input:disabled {
    cursor: not-allowed;
    resize: block;
    background-color: var(--jp-layout-color2);
    color: var(--jp-ui-font-color2);
    }

    .jp-InputGroup input:disabled ~ span {
    cursor: not-allowed;
    color: var(--jp-ui-font-color2);
    }

    .jp-InputGroup input::placeholder,
    input::placeholder {
    color: var(--jp-ui-font-color2);
    }

    .jp-InputGroupAction {
    position: absolute;
    bottom: 1px;
    right: 0;
    padding: 6px;
    }

    .jp-HTMLSelect.jp-DefaultStyle select {
    background-color: initial;
    border: none;
    border-radius: 0;
    box-shadow: none;
    color: var(--jp-ui-font-color0);
    display: block;
    font-size: var(--jp-ui-font-size1);
    font-family: var(--jp-ui-font-family);
    height: 24px;
    line-height: 14px;
    padding: 0 25px 0 10px;
    text-align: left;
    -moz-appearance: none;
    -webkit-appearance: none;
    }

    .jp-HTMLSelect.jp-DefaultStyle select:disabled {
    background-color: var(--jp-layout-color2);
    color: var(--jp-ui-font-color2);
    cursor: not-allowed;
    resize: block;
    }

    .jp-HTMLSelect.jp-DefaultStyle select:disabled ~ span {
    cursor: not-allowed;
    }

    /* Use our own theme for hover and option styles */
    /* stylelint-disable-next-line selector-max-type */
    .jp-HTMLSelect.jp-DefaultStyle select:hover,
    .jp-HTMLSelect.jp-DefaultStyle select > option {
    background-color: var(--jp-layout-color2);
    color: var(--jp-ui-font-color0);
    }

    select {
    box-sizing: border-box;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Styles
    |----------------------------------------------------------------------------*/

    .jp-StatusBar-Widget {
    display: flex;
    align-items: center;
    background: var(--jp-layout-color2);
    min-height: var(--jp-statusbar-height);
    justify-content: space-between;
    padding: 0 10px;
    }

    .jp-StatusBar-Left {
    display: flex;
    align-items: center;
    flex-direction: row;
    }

    .jp-StatusBar-Middle {
    display: flex;
    align-items: center;
    }

    .jp-StatusBar-Right {
    display: flex;
    align-items: center;
    flex-direction: row-reverse;
    }

    .jp-StatusBar-Item {
    max-height: var(--jp-statusbar-height);
    margin: 0 2px;
    height: var(--jp-statusbar-height);
    white-space: nowrap;
    text-overflow: ellipsis;
    color: var(--jp-ui-font-color1);
    padding: 0 6px;
    }

    .jp-mod-highlighted:hover {
    background-color: var(--jp-layout-color3);
    }

    .jp-mod-clicked {
    background-color: var(--jp-brand-color1);
    }

    .jp-mod-clicked:hover {
    background-color: var(--jp-brand-color0);
    }

    .jp-mod-clicked .jp-StatusBar-TextItem {
    color: var(--jp-ui-inverse-font-color1);
    }

    .jp-StatusBar-HoverItem {
    box-shadow: '0px 4px 4px rgba(0, 0, 0, 0.25)';
    }

    .jp-StatusBar-TextItem {
    font-size: var(--jp-ui-font-size1);
    font-family: var(--jp-ui-font-family);
    line-height: 24px;
    color: var(--jp-ui-font-color1);
    }

    .jp-StatusBar-GroupItem {
    display: flex;
    align-items: center;
    flex-direction: row;
    }

    .jp-Statusbar-ProgressCircle svg {
    display: block;
    margin: 0 auto;
    width: 16px;
    height: 24px;
    align-self: normal;
    }

    .jp-Statusbar-ProgressCircle path {
    fill: var(--jp-inverse-layout-color3);
    }

    .jp-Statusbar-ProgressBar-progress-bar {
    height: 10px;
    width: 100px;
    border: solid 0.25px var(--jp-brand-color2);
    border-radius: 3px;
    overflow: hidden;
    align-self: center;
    }

    .jp-Statusbar-ProgressBar-progress-bar > div {
    background-color: var(--jp-brand-color2);
    background-image: linear-gradient(
        -45deg,
        rgba(255, 255, 255, 0.2) 25%,
        transparent 25%,
        transparent 50%,
        rgba(255, 255, 255, 0.2) 50%,
        rgba(255, 255, 255, 0.2) 75%,
        transparent 75%,
        transparent
    );
    background-size: 40px 40px;
    float: left;
    width: 0%;
    height: 100%;
    font-size: 12px;
    line-height: 14px;
    color: #fff;
    text-align: center;
    animation: jp-Statusbar-ExecutionTime-progress-bar 2s linear infinite;
    }

    .jp-Statusbar-ProgressBar-progress-bar p {
    color: var(--jp-ui-font-color1);
    font-family: var(--jp-ui-font-family);
    font-size: var(--jp-ui-font-size1);
    line-height: 10px;
    width: 100px;
    }

    @keyframes jp-Statusbar-ExecutionTime-progress-bar {
    0% {
        background-position: 0 0;
    }

    100% {
        background-position: 40px 40px;
    }
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Variables
    |----------------------------------------------------------------------------*/

    :root {
    --jp-private-commandpalette-search-height: 28px;
    }

    /*-----------------------------------------------------------------------------
    | Overall styles
    |----------------------------------------------------------------------------*/

    .lm-CommandPalette {
    padding-bottom: 0;
    color: var(--jp-ui-font-color1);
    background: var(--jp-layout-color1);

    /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
    font-size: var(--jp-ui-font-size1);
    }

    /*-----------------------------------------------------------------------------
    | Modal variant
    |----------------------------------------------------------------------------*/

    .jp-ModalCommandPalette {
    position: absolute;
    z-index: 10000;
    top: 38px;
    left: 30%;
    margin: 0;
    padding: 4px;
    width: 40%;
    box-shadow: var(--jp-elevation-z4);
    border-radius: 4px;
    background: var(--jp-layout-color0);
    }

    .jp-ModalCommandPalette .lm-CommandPalette {
    max-height: 40vh;
    }

    .jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
    display: none;
    }

    .jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
    display: none;
    }

    .jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
    margin-left: 4px;
    margin-right: 4px;
    }

    .jp-ModalCommandPalette
    .lm-CommandPalette
    .lm-CommandPalette-item.lm-mod-disabled {
    display: none;
    }

    /*-----------------------------------------------------------------------------
    | Search
    |----------------------------------------------------------------------------*/

    .lm-CommandPalette-search {
    padding: 4px;
    background-color: var(--jp-layout-color1);
    z-index: 2;
    }

    .lm-CommandPalette-wrapper {
    overflow: overlay;
    padding: 0 9px;
    background-color: var(--jp-input-active-background);
    height: 30px;
    box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
    }

    .lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
    box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
        inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
    }

    .jp-SearchIconGroup {
    color: white;
    background-color: var(--jp-brand-color1);
    position: absolute;
    top: 4px;
    right: 4px;
    padding: 5px 5px 1px;
    }

    .jp-SearchIconGroup svg {
    height: 20px;
    width: 20px;
    }

    .jp-SearchIconGroup .jp-icon3[fill] {
    fill: var(--jp-layout-color0);
    }

    .lm-CommandPalette-input {
    background: transparent;
    width: calc(100% - 18px);
    float: left;
    border: none;
    outline: none;
    font-size: var(--jp-ui-font-size1);
    color: var(--jp-ui-font-color0);
    line-height: var(--jp-private-commandpalette-search-height);
    }

    .lm-CommandPalette-input::-webkit-input-placeholder,
    .lm-CommandPalette-input::-moz-placeholder,
    .lm-CommandPalette-input:-ms-input-placeholder {
    color: var(--jp-ui-font-color2);
    font-size: var(--jp-ui-font-size1);
    }

    /*-----------------------------------------------------------------------------
    | Results
    |----------------------------------------------------------------------------*/

    .lm-CommandPalette-header:first-child {
    margin-top: 0;
    }

    .lm-CommandPalette-header {
    border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
    color: var(--jp-ui-font-color1);
    cursor: pointer;
    display: flex;
    font-size: var(--jp-ui-font-size0);
    font-weight: 600;
    letter-spacing: 1px;
    margin-top: 8px;
    padding: 8px 0 8px 12px;
    text-transform: uppercase;
    }

    .lm-CommandPalette-header.lm-mod-active {
    background: var(--jp-layout-color2);
    }

    .lm-CommandPalette-header > mark {
    background-color: transparent;
    font-weight: bold;
    color: var(--jp-ui-font-color1);
    }

    .lm-CommandPalette-item {
    padding: 4px 12px 4px 4px;
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    font-weight: 400;
    display: flex;
    }

    .lm-CommandPalette-item.lm-mod-disabled {
    color: var(--jp-ui-font-color2);
    }

    .lm-CommandPalette-item.lm-mod-active {
    color: var(--jp-ui-inverse-font-color1);
    background: var(--jp-brand-color1);
    }

    .lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
    color: var(--jp-ui-inverse-font-color0);
    }

    .lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
    fill: var(--jp-layout-color0);
    }

    .lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
    color: var(--jp-ui-inverse-font-color1);
    background: var(--jp-brand-color1);
    }

    .lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
    background: var(--jp-layout-color2);
    }

    .lm-CommandPalette-itemContent {
    overflow: hidden;
    }

    .lm-CommandPalette-itemLabel > mark {
    color: var(--jp-ui-font-color0);
    background-color: transparent;
    font-weight: bold;
    }

    .lm-CommandPalette-item.lm-mod-disabled mark {
    color: var(--jp-ui-font-color2);
    }

    .lm-CommandPalette-item .lm-CommandPalette-itemIcon {
    margin: 0 4px 0 0;
    position: relative;
    width: 16px;
    top: 2px;
    flex: 0 0 auto;
    }

    .lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
    opacity: 0.6;
    }

    .lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
    flex: 0 0 auto;
    }

    .lm-CommandPalette-itemCaption {
    display: none;
    }

    .lm-CommandPalette-content {
    background-color: var(--jp-layout-color1);
    }

    .lm-CommandPalette-content:empty::after {
    content: 'No results';
    margin: auto;
    margin-top: 20px;
    width: 100px;
    display: block;
    font-size: var(--jp-ui-font-size2);
    font-family: var(--jp-ui-font-family);
    font-weight: lighter;
    }

    .lm-CommandPalette-emptyMessage {
    text-align: center;
    margin-top: 24px;
    line-height: 1.32;
    padding: 0 8px;
    color: var(--jp-content-font-color3);
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) 2014-2017, Jupyter Development Team.
    |
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-Dialog {
    position: absolute;
    z-index: 10000;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    top: 0;
    left: 0;
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    background: var(--jp-dialog-background);
    }

    .jp-Dialog-content {
    display: flex;
    flex-direction: column;
    margin-left: auto;
    margin-right: auto;
    background: var(--jp-layout-color1);
    padding: 24px 24px 12px;
    min-width: 300px;
    min-height: 150px;
    max-width: 1000px;
    max-height: 500px;
    box-sizing: border-box;
    box-shadow: var(--jp-elevation-z20);
    word-wrap: break-word;
    border-radius: var(--jp-border-radius);

    /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
    font-size: var(--jp-ui-font-size1);
    color: var(--jp-ui-font-color1);
    resize: both;
    }

    .jp-Dialog-content.jp-Dialog-content-small {
    max-width: 500px;
    }

    .jp-Dialog-button {
    overflow: visible;
    }

    button.jp-Dialog-button:focus {
    outline: 1px solid var(--jp-brand-color1);
    outline-offset: 4px;
    -moz-outline-radius: 0;
    }

    button.jp-Dialog-button:focus::-moz-focus-inner {
    border: 0;
    }

    button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus,
    button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus,
    button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
    outline-offset: 4px;
    -moz-outline-radius: 0;
    }

    button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus {
    outline: 1px solid var(--jp-accept-color-normal, var(--jp-brand-color1));
    }

    button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus {
    outline: 1px solid var(--jp-warn-color-normal, var(--jp-error-color1));
    }

    button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
    outline: 1px solid var(--jp-reject-color-normal, var(--md-grey-600));
    }

    button.jp-Dialog-close-button {
    padding: 0;
    height: 100%;
    min-width: unset;
    min-height: unset;
    }

    .jp-Dialog-header {
    display: flex;
    justify-content: space-between;
    flex: 0 0 auto;
    padding-bottom: 12px;
    font-size: var(--jp-ui-font-size3);
    font-weight: 400;
    color: var(--jp-ui-font-color1);
    }

    .jp-Dialog-body {
    display: flex;
    flex-direction: column;
    flex: 1 1 auto;
    font-size: var(--jp-ui-font-size1);
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    overflow: auto;
    }

    .jp-Dialog-footer {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    flex: 0 0 auto;
    margin-left: -12px;
    margin-right: -12px;
    padding: 12px;
    }

    .jp-Dialog-checkbox {
    padding-right: 5px;
    }

    .jp-Dialog-checkbox > input:focus-visible {
    outline: 1px solid var(--jp-input-active-border-color);
    outline-offset: 1px;
    }

    .jp-Dialog-spacer {
    flex: 1 1 auto;
    }

    .jp-Dialog-title {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    }

    .jp-Dialog-body > .jp-select-wrapper {
    width: 100%;
    }

    .jp-Dialog-body > button {
    padding: 0 16px;
    }

    .jp-Dialog-body > label {
    line-height: 1.4;
    color: var(--jp-ui-font-color0);
    }

    .jp-Dialog-button.jp-mod-styled:not(:last-child) {
    margin-right: 12px;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    .jp-Input-Boolean-Dialog {
    flex-direction: row-reverse;
    align-items: end;
    width: 100%;
    }

    .jp-Input-Boolean-Dialog > label {
    flex: 1 1 auto;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) 2014-2016, Jupyter Development Team.
    |
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-MainAreaWidget > :focus {
    outline: none;
    }

    .jp-MainAreaWidget .jp-MainAreaWidget-error {
    padding: 6px;
    }

    .jp-MainAreaWidget .jp-MainAreaWidget-error > pre {
    width: auto;
    padding: 10px;
    background: var(--jp-error-color3);
    border: var(--jp-border-width) solid var(--jp-error-color1);
    border-radius: var(--jp-border-radius);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    white-space: pre-wrap;
    word-wrap: break-word;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /**
    * google-material-color v1.2.6
    * https://github.com/danlevan/google-material-color
    */
    :root {
    --md-red-50: #ffebee;
    --md-red-100: #ffcdd2;
    --md-red-200: #ef9a9a;
    --md-red-300: #e57373;
    --md-red-400: #ef5350;
    --md-red-500: #f44336;
    --md-red-600: #e53935;
    --md-red-700: #d32f2f;
    --md-red-800: #c62828;
    --md-red-900: #b71c1c;
    --md-red-A100: #ff8a80;
    --md-red-A200: #ff5252;
    --md-red-A400: #ff1744;
    --md-red-A700: #d50000;
    --md-pink-50: #fce4ec;
    --md-pink-100: #f8bbd0;
    --md-pink-200: #f48fb1;
    --md-pink-300: #f06292;
    --md-pink-400: #ec407a;
    --md-pink-500: #e91e63;
    --md-pink-600: #d81b60;
    --md-pink-700: #c2185b;
    --md-pink-800: #ad1457;
    --md-pink-900: #880e4f;
    --md-pink-A100: #ff80ab;
    --md-pink-A200: #ff4081;
    --md-pink-A400: #f50057;
    --md-pink-A700: #c51162;
    --md-purple-50: #f3e5f5;
    --md-purple-100: #e1bee7;
    --md-purple-200: #ce93d8;
    --md-purple-300: #ba68c8;
    --md-purple-400: #ab47bc;
    --md-purple-500: #9c27b0;
    --md-purple-600: #8e24aa;
    --md-purple-700: #7b1fa2;
    --md-purple-800: #6a1b9a;
    --md-purple-900: #4a148c;
    --md-purple-A100: #ea80fc;
    --md-purple-A200: #e040fb;
    --md-purple-A400: #d500f9;
    --md-purple-A700: #a0f;
    --md-deep-purple-50: #ede7f6;
    --md-deep-purple-100: #d1c4e9;
    --md-deep-purple-200: #b39ddb;
    --md-deep-purple-300: #9575cd;
    --md-deep-purple-400: #7e57c2;
    --md-deep-purple-500: #673ab7;
    --md-deep-purple-600: #5e35b1;
    --md-deep-purple-700: #512da8;
    --md-deep-purple-800: #4527a0;
    --md-deep-purple-900: #311b92;
    --md-deep-purple-A100: #b388ff;
    --md-deep-purple-A200: #7c4dff;
    --md-deep-purple-A400: #651fff;
    --md-deep-purple-A700: #6200ea;
    --md-indigo-50: #e8eaf6;
    --md-indigo-100: #c5cae9;
    --md-indigo-200: #9fa8da;
    --md-indigo-300: #7986cb;
    --md-indigo-400: #5c6bc0;
    --md-indigo-500: #3f51b5;
    --md-indigo-600: #3949ab;
    --md-indigo-700: #303f9f;
    --md-indigo-800: #283593;
    --md-indigo-900: #1a237e;
    --md-indigo-A100: #8c9eff;
    --md-indigo-A200: #536dfe;
    --md-indigo-A400: #3d5afe;
    --md-indigo-A700: #304ffe;
    --md-blue-50: #e3f2fd;
    --md-blue-100: #bbdefb;
    --md-blue-200: #90caf9;
    --md-blue-300: #64b5f6;
    --md-blue-400: #42a5f5;
    --md-blue-500: #2196f3;
    --md-blue-600: #1e88e5;
    --md-blue-700: #1976d2;
    --md-blue-800: #1565c0;
    --md-blue-900: #0d47a1;
    --md-blue-A100: #82b1ff;
    --md-blue-A200: #448aff;
    --md-blue-A400: #2979ff;
    --md-blue-A700: #2962ff;
    --md-light-blue-50: #e1f5fe;
    --md-light-blue-100: #b3e5fc;
    --md-light-blue-200: #81d4fa;
    --md-light-blue-300: #4fc3f7;
    --md-light-blue-400: #29b6f6;
    --md-light-blue-500: #03a9f4;
    --md-light-blue-600: #039be5;
    --md-light-blue-700: #0288d1;
    --md-light-blue-800: #0277bd;
    --md-light-blue-900: #01579b;
    --md-light-blue-A100: #80d8ff;
    --md-light-blue-A200: #40c4ff;
    --md-light-blue-A400: #00b0ff;
    --md-light-blue-A700: #0091ea;
    --md-cyan-50: #e0f7fa;
    --md-cyan-100: #b2ebf2;
    --md-cyan-200: #80deea;
    --md-cyan-300: #4dd0e1;
    --md-cyan-400: #26c6da;
    --md-cyan-500: #00bcd4;
    --md-cyan-600: #00acc1;
    --md-cyan-700: #0097a7;
    --md-cyan-800: #00838f;
    --md-cyan-900: #006064;
    --md-cyan-A100: #84ffff;
    --md-cyan-A200: #18ffff;
    --md-cyan-A400: #00e5ff;
    --md-cyan-A700: #00b8d4;
    --md-teal-50: #e0f2f1;
    --md-teal-100: #b2dfdb;
    --md-teal-200: #80cbc4;
    --md-teal-300: #4db6ac;
    --md-teal-400: #26a69a;
    --md-teal-500: #009688;
    --md-teal-600: #00897b;
    --md-teal-700: #00796b;
    --md-teal-800: #00695c;
    --md-teal-900: #004d40;
    --md-teal-A100: #a7ffeb;
    --md-teal-A200: #64ffda;
    --md-teal-A400: #1de9b6;
    --md-teal-A700: #00bfa5;
    --md-green-50: #e8f5e9;
    --md-green-100: #c8e6c9;
    --md-green-200: #a5d6a7;
    --md-green-300: #81c784;
    --md-green-400: #66bb6a;
    --md-green-500: #4caf50;
    --md-green-600: #43a047;
    --md-green-700: #388e3c;
    --md-green-800: #2e7d32;
    --md-green-900: #1b5e20;
    --md-green-A100: #b9f6ca;
    --md-green-A200: #69f0ae;
    --md-green-A400: #00e676;
    --md-green-A700: #00c853;
    --md-light-green-50: #f1f8e9;
    --md-light-green-100: #dcedc8;
    --md-light-green-200: #c5e1a5;
    --md-light-green-300: #aed581;
    --md-light-green-400: #9ccc65;
    --md-light-green-500: #8bc34a;
    --md-light-green-600: #7cb342;
    --md-light-green-700: #689f38;
    --md-light-green-800: #558b2f;
    --md-light-green-900: #33691e;
    --md-light-green-A100: #ccff90;
    --md-light-green-A200: #b2ff59;
    --md-light-green-A400: #76ff03;
    --md-light-green-A700: #64dd17;
    --md-lime-50: #f9fbe7;
    --md-lime-100: #f0f4c3;
    --md-lime-200: #e6ee9c;
    --md-lime-300: #dce775;
    --md-lime-400: #d4e157;
    --md-lime-500: #cddc39;
    --md-lime-600: #c0ca33;
    --md-lime-700: #afb42b;
    --md-lime-800: #9e9d24;
    --md-lime-900: #827717;
    --md-lime-A100: #f4ff81;
    --md-lime-A200: #eeff41;
    --md-lime-A400: #c6ff00;
    --md-lime-A700: #aeea00;
    --md-yellow-50: #fffde7;
    --md-yellow-100: #fff9c4;
    --md-yellow-200: #fff59d;
    --md-yellow-300: #fff176;
    --md-yellow-400: #ffee58;
    --md-yellow-500: #ffeb3b;
    --md-yellow-600: #fdd835;
    --md-yellow-700: #fbc02d;
    --md-yellow-800: #f9a825;
    --md-yellow-900: #f57f17;
    --md-yellow-A100: #ffff8d;
    --md-yellow-A200: #ff0;
    --md-yellow-A400: #ffea00;
    --md-yellow-A700: #ffd600;
    --md-amber-50: #fff8e1;
    --md-amber-100: #ffecb3;
    --md-amber-200: #ffe082;
    --md-amber-300: #ffd54f;
    --md-amber-400: #ffca28;
    --md-amber-500: #ffc107;
    --md-amber-600: #ffb300;
    --md-amber-700: #ffa000;
    --md-amber-800: #ff8f00;
    --md-amber-900: #ff6f00;
    --md-amber-A100: #ffe57f;
    --md-amber-A200: #ffd740;
    --md-amber-A400: #ffc400;
    --md-amber-A700: #ffab00;
    --md-orange-50: #fff3e0;
    --md-orange-100: #ffe0b2;
    --md-orange-200: #ffcc80;
    --md-orange-300: #ffb74d;
    --md-orange-400: #ffa726;
    --md-orange-500: #ff9800;
    --md-orange-600: #fb8c00;
    --md-orange-700: #f57c00;
    --md-orange-800: #ef6c00;
    --md-orange-900: #e65100;
    --md-orange-A100: #ffd180;
    --md-orange-A200: #ffab40;
    --md-orange-A400: #ff9100;
    --md-orange-A700: #ff6d00;
    --md-deep-orange-50: #fbe9e7;
    --md-deep-orange-100: #ffccbc;
    --md-deep-orange-200: #ffab91;
    --md-deep-orange-300: #ff8a65;
    --md-deep-orange-400: #ff7043;
    --md-deep-orange-500: #ff5722;
    --md-deep-orange-600: #f4511e;
    --md-deep-orange-700: #e64a19;
    --md-deep-orange-800: #d84315;
    --md-deep-orange-900: #bf360c;
    --md-deep-orange-A100: #ff9e80;
    --md-deep-orange-A200: #ff6e40;
    --md-deep-orange-A400: #ff3d00;
    --md-deep-orange-A700: #dd2c00;
    --md-brown-50: #efebe9;
    --md-brown-100: #d7ccc8;
    --md-brown-200: #bcaaa4;
    --md-brown-300: #a1887f;
    --md-brown-400: #8d6e63;
    --md-brown-500: #795548;
    --md-brown-600: #6d4c41;
    --md-brown-700: #5d4037;
    --md-brown-800: #4e342e;
    --md-brown-900: #3e2723;
    --md-grey-50: #fafafa;
    --md-grey-100: #f5f5f5;
    --md-grey-200: #eee;
    --md-grey-300: #e0e0e0;
    --md-grey-400: #bdbdbd;
    --md-grey-500: #9e9e9e;
    --md-grey-600: #757575;
    --md-grey-700: #616161;
    --md-grey-800: #424242;
    --md-grey-900: #212121;
    --md-blue-grey-50: #eceff1;
    --md-blue-grey-100: #cfd8dc;
    --md-blue-grey-200: #b0bec5;
    --md-blue-grey-300: #90a4ae;
    --md-blue-grey-400: #78909c;
    --md-blue-grey-500: #607d8b;
    --md-blue-grey-600: #546e7a;
    --md-blue-grey-700: #455a64;
    --md-blue-grey-800: #37474f;
    --md-blue-grey-900: #263238;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) 2014-2017, Jupyter Development Team.
    |
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | RenderedText
    |----------------------------------------------------------------------------*/

    :root {
    /* This is the padding value to fill the gaps between lines containing spans with background color. */
    --jp-private-code-span-padding: calc(
        (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
    );
    }

    .jp-RenderedText {
    text-align: left;
    padding-left: var(--jp-code-padding);
    line-height: var(--jp-code-line-height);
    font-family: var(--jp-code-font-family);
    }

    .jp-RenderedText pre,
    .jp-RenderedJavaScript pre,
    .jp-RenderedHTMLCommon pre {
    color: var(--jp-content-font-color1);
    font-size: var(--jp-code-font-size);
    border: none;
    margin: 0;
    padding: 0;
    }

    .jp-RenderedText pre a:link {
    text-decoration: none;
    color: var(--jp-content-link-color);
    }

    .jp-RenderedText pre a:hover {
    text-decoration: underline;
    color: var(--jp-content-link-color);
    }

    .jp-RenderedText pre a:visited {
    text-decoration: none;
    color: var(--jp-content-link-color);
    }

    /* console foregrounds and backgrounds */
    .jp-RenderedText pre .ansi-black-fg {
    color: #3e424d;
    }

    .jp-RenderedText pre .ansi-red-fg {
    color: #e75c58;
    }

    .jp-RenderedText pre .ansi-green-fg {
    color: #00a250;
    }

    .jp-RenderedText pre .ansi-yellow-fg {
    color: #ddb62b;
    }

    .jp-RenderedText pre .ansi-blue-fg {
    color: #208ffb;
    }

    .jp-RenderedText pre .ansi-magenta-fg {
    color: #d160c4;
    }

    .jp-RenderedText pre .ansi-cyan-fg {
    color: #60c6c8;
    }

    .jp-RenderedText pre .ansi-white-fg {
    color: #c5c1b4;
    }

    .jp-RenderedText pre .ansi-black-bg {
    background-color: #3e424d;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-red-bg {
    background-color: #e75c58;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-green-bg {
    background-color: #00a250;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-yellow-bg {
    background-color: #ddb62b;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-blue-bg {
    background-color: #208ffb;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-magenta-bg {
    background-color: #d160c4;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-cyan-bg {
    background-color: #60c6c8;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-white-bg {
    background-color: #c5c1b4;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-black-intense-fg {
    color: #282c36;
    }

    .jp-RenderedText pre .ansi-red-intense-fg {
    color: #b22b31;
    }

    .jp-RenderedText pre .ansi-green-intense-fg {
    color: #007427;
    }

    .jp-RenderedText pre .ansi-yellow-intense-fg {
    color: #b27d12;
    }

    .jp-RenderedText pre .ansi-blue-intense-fg {
    color: #0065ca;
    }

    .jp-RenderedText pre .ansi-magenta-intense-fg {
    color: #a03196;
    }

    .jp-RenderedText pre .ansi-cyan-intense-fg {
    color: #258f8f;
    }

    .jp-RenderedText pre .ansi-white-intense-fg {
    color: #a1a6b2;
    }

    .jp-RenderedText pre .ansi-black-intense-bg {
    background-color: #282c36;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-red-intense-bg {
    background-color: #b22b31;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-green-intense-bg {
    background-color: #007427;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-yellow-intense-bg {
    background-color: #b27d12;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-blue-intense-bg {
    background-color: #0065ca;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-magenta-intense-bg {
    background-color: #a03196;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-cyan-intense-bg {
    background-color: #258f8f;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-white-intense-bg {
    background-color: #a1a6b2;
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-default-inverse-fg {
    color: var(--jp-ui-inverse-font-color0);
    }

    .jp-RenderedText pre .ansi-default-inverse-bg {
    background-color: var(--jp-inverse-layout-color0);
    padding: var(--jp-private-code-span-padding) 0;
    }

    .jp-RenderedText pre .ansi-bold {
    font-weight: bold;
    }

    .jp-RenderedText pre .ansi-underline {
    text-decoration: underline;
    }

    .jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
    background: var(--jp-rendermime-error-background);
    padding-top: var(--jp-code-padding);
    }

    /*-----------------------------------------------------------------------------
    | RenderedLatex
    |----------------------------------------------------------------------------*/

    .jp-RenderedLatex {
    color: var(--jp-content-font-color1);
    font-size: var(--jp-content-font-size1);
    line-height: var(--jp-content-line-height);
    }

    /* Left-justify outputs.*/
    .jp-OutputArea-output.jp-RenderedLatex {
    padding: var(--jp-code-padding);
    text-align: left;
    }

    /*-----------------------------------------------------------------------------
    | RenderedHTML
    |----------------------------------------------------------------------------*/

    .jp-RenderedHTMLCommon {
    color: var(--jp-content-font-color1);
    font-family: var(--jp-content-font-family);
    font-size: var(--jp-content-font-size1);
    line-height: var(--jp-content-line-height);

    /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
    padding-right: 20px;
    }

    .jp-RenderedHTMLCommon em {
    font-style: italic;
    }

    .jp-RenderedHTMLCommon strong {
    font-weight: bold;
    }

    .jp-RenderedHTMLCommon u {
    text-decoration: underline;
    }

    .jp-RenderedHTMLCommon a:link {
    text-decoration: none;
    color: var(--jp-content-link-color);
    }

    .jp-RenderedHTMLCommon a:hover {
    text-decoration: underline;
    color: var(--jp-content-link-color);
    }

    .jp-RenderedHTMLCommon a:visited {
    text-decoration: none;
    color: var(--jp-content-link-color);
    }

    /* Headings */

    .jp-RenderedHTMLCommon h1,
    .jp-RenderedHTMLCommon h2,
    .jp-RenderedHTMLCommon h3,
    .jp-RenderedHTMLCommon h4,
    .jp-RenderedHTMLCommon h5,
    .jp-RenderedHTMLCommon h6 {
    line-height: var(--jp-content-heading-line-height);
    font-weight: var(--jp-content-heading-font-weight);
    font-style: normal;
    margin: var(--jp-content-heading-margin-top) 0
        var(--jp-content-heading-margin-bottom) 0;
    }

    .jp-RenderedHTMLCommon h1:first-child,
    .jp-RenderedHTMLCommon h2:first-child,
    .jp-RenderedHTMLCommon h3:first-child,
    .jp-RenderedHTMLCommon h4:first-child,
    .jp-RenderedHTMLCommon h5:first-child,
    .jp-RenderedHTMLCommon h6:first-child {
    margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
    }

    .jp-RenderedHTMLCommon h1:last-child,
    .jp-RenderedHTMLCommon h2:last-child,
    .jp-RenderedHTMLCommon h3:last-child,
    .jp-RenderedHTMLCommon h4:last-child,
    .jp-RenderedHTMLCommon h5:last-child,
    .jp-RenderedHTMLCommon h6:last-child {
    margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
    }

    .jp-RenderedHTMLCommon h1 {
    font-size: var(--jp-content-font-size5);
    }

    .jp-RenderedHTMLCommon h2 {
    font-size: var(--jp-content-font-size4);
    }

    .jp-RenderedHTMLCommon h3 {
    font-size: var(--jp-content-font-size3);
    }

    .jp-RenderedHTMLCommon h4 {
    font-size: var(--jp-content-font-size2);
    }

    .jp-RenderedHTMLCommon h5 {
    font-size: var(--jp-content-font-size1);
    }

    .jp-RenderedHTMLCommon h6 {
    font-size: var(--jp-content-font-size0);
    }

    /* Lists */

    /* stylelint-disable selector-max-type, selector-max-compound-selectors */

    .jp-RenderedHTMLCommon ul:not(.list-inline),
    .jp-RenderedHTMLCommon ol:not(.list-inline) {
    padding-left: 2em;
    }

    .jp-RenderedHTMLCommon ul {
    list-style: disc;
    }

    .jp-RenderedHTMLCommon ul ul {
    list-style: square;
    }

    .jp-RenderedHTMLCommon ul ul ul {
    list-style: circle;
    }

    .jp-RenderedHTMLCommon ol {
    list-style: decimal;
    }

    .jp-RenderedHTMLCommon ol ol {
    list-style: upper-alpha;
    }

    .jp-RenderedHTMLCommon ol ol ol {
    list-style: lower-alpha;
    }

    .jp-RenderedHTMLCommon ol ol ol ol {
    list-style: lower-roman;
    }

    .jp-RenderedHTMLCommon ol ol ol ol ol {
    list-style: decimal;
    }

    .jp-RenderedHTMLCommon ol,
    .jp-RenderedHTMLCommon ul {
    margin-bottom: 1em;
    }

    .jp-RenderedHTMLCommon ul ul,
    .jp-RenderedHTMLCommon ul ol,
    .jp-RenderedHTMLCommon ol ul,
    .jp-RenderedHTMLCommon ol ol {
    margin-bottom: 0;
    }

    /* stylelint-enable selector-max-type, selector-max-compound-selectors */

    .jp-RenderedHTMLCommon hr {
    color: var(--jp-border-color2);
    background-color: var(--jp-border-color1);
    margin-top: 1em;
    margin-bottom: 1em;
    }

    .jp-RenderedHTMLCommon > pre {
    margin: 1.5em 2em;
    }

    .jp-RenderedHTMLCommon pre,
    .jp-RenderedHTMLCommon code {
    border: 0;
    background-color: var(--jp-layout-color0);
    color: var(--jp-content-font-color1);
    font-family: var(--jp-code-font-family);
    font-size: inherit;
    line-height: var(--jp-code-line-height);
    padding: 0;
    white-space: pre-wrap;
    }

    .jp-RenderedHTMLCommon :not(pre) > code {
    background-color: var(--jp-layout-color2);
    padding: 1px 5px;
    }

    /* Tables */

    .jp-RenderedHTMLCommon table {
    border-collapse: collapse;
    border-spacing: 0;
    border: none;
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    table-layout: fixed;
    margin-left: auto;
    margin-bottom: 1em;
    margin-right: auto;
    }

    .jp-RenderedHTMLCommon thead {
    border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
    vertical-align: bottom;
    }

    .jp-RenderedHTMLCommon td,
    .jp-RenderedHTMLCommon th,
    .jp-RenderedHTMLCommon tr {
    vertical-align: middle;
    padding: 0.5em;
    line-height: normal;
    white-space: normal;
    max-width: none;
    border: none;
    }

    .jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
    .jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
    max-width: none;
    }

    :not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
    :not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
    :not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
    text-align: right;
    }

    .jp-RenderedHTMLCommon th {
    font-weight: bold;
    }

    .jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
    background: var(--jp-layout-color0);
    }

    .jp-RenderedHTMLCommon tbody tr:nth-child(even) {
    background: var(--jp-rendermime-table-row-background);
    }

    .jp-RenderedHTMLCommon tbody tr:hover {
    background: var(--jp-rendermime-table-row-hover-background);
    }

    .jp-RenderedHTMLCommon p {
    text-align: left;
    margin: 0;
    margin-bottom: 1em;
    }

    .jp-RenderedHTMLCommon img {
    -moz-force-broken-image-icon: 1;
    }

    /* Restrict to direct children as other images could be nested in other content. */
    .jp-RenderedHTMLCommon > img {
    display: block;
    margin-left: 0;
    margin-right: 0;
    margin-bottom: 1em;
    }

    /* Change color behind transparent images if they need it... */
    [data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
    background-color: var(--jp-inverse-layout-color1);
    }

    [data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
    background-color: var(--jp-inverse-layout-color1);
    }

    .jp-RenderedHTMLCommon img,
    .jp-RenderedImage img,
    .jp-RenderedHTMLCommon svg,
    .jp-RenderedSVG svg {
    max-width: 100%;
    height: auto;
    }

    .jp-RenderedHTMLCommon img.jp-mod-unconfined,
    .jp-RenderedImage img.jp-mod-unconfined,
    .jp-RenderedHTMLCommon svg.jp-mod-unconfined,
    .jp-RenderedSVG svg.jp-mod-unconfined {
    max-width: none;
    }

    .jp-RenderedHTMLCommon .alert {
    padding: var(--jp-notebook-padding);
    border: var(--jp-border-width) solid transparent;
    border-radius: var(--jp-border-radius);
    margin-bottom: 1em;
    }

    .jp-RenderedHTMLCommon .alert-info {
    color: var(--jp-info-color0);
    background-color: var(--jp-info-color3);
    border-color: var(--jp-info-color2);
    }

    .jp-RenderedHTMLCommon .alert-info hr {
    border-color: var(--jp-info-color3);
    }

    .jp-RenderedHTMLCommon .alert-info > p:last-child,
    .jp-RenderedHTMLCommon .alert-info > ul:last-child {
    margin-bottom: 0;
    }

    .jp-RenderedHTMLCommon .alert-warning {
    color: var(--jp-warn-color0);
    background-color: var(--jp-warn-color3);
    border-color: var(--jp-warn-color2);
    }

    .jp-RenderedHTMLCommon .alert-warning hr {
    border-color: var(--jp-warn-color3);
    }

    .jp-RenderedHTMLCommon .alert-warning > p:last-child,
    .jp-RenderedHTMLCommon .alert-warning > ul:last-child {
    margin-bottom: 0;
    }

    .jp-RenderedHTMLCommon .alert-success {
    color: var(--jp-success-color0);
    background-color: var(--jp-success-color3);
    border-color: var(--jp-success-color2);
    }

    .jp-RenderedHTMLCommon .alert-success hr {
    border-color: var(--jp-success-color3);
    }

    .jp-RenderedHTMLCommon .alert-success > p:last-child,
    .jp-RenderedHTMLCommon .alert-success > ul:last-child {
    margin-bottom: 0;
    }

    .jp-RenderedHTMLCommon .alert-danger {
    color: var(--jp-error-color0);
    background-color: var(--jp-error-color3);
    border-color: var(--jp-error-color2);
    }

    .jp-RenderedHTMLCommon .alert-danger hr {
    border-color: var(--jp-error-color3);
    }

    .jp-RenderedHTMLCommon .alert-danger > p:last-child,
    .jp-RenderedHTMLCommon .alert-danger > ul:last-child {
    margin-bottom: 0;
    }

    .jp-RenderedHTMLCommon blockquote {
    margin: 1em 2em;
    padding: 0 1em;
    border-left: 5px solid var(--jp-border-color2);
    }

    a.jp-InternalAnchorLink {
    visibility: hidden;
    margin-left: 8px;
    color: var(--md-blue-800);
    }

    h1:hover .jp-InternalAnchorLink,
    h2:hover .jp-InternalAnchorLink,
    h3:hover .jp-InternalAnchorLink,
    h4:hover .jp-InternalAnchorLink,
    h5:hover .jp-InternalAnchorLink,
    h6:hover .jp-InternalAnchorLink {
    visibility: visible;
    }

    .jp-RenderedHTMLCommon kbd {
    background-color: var(--jp-rendermime-table-row-background);
    border: 1px solid var(--jp-border-color0);
    border-bottom-color: var(--jp-border-color2);
    border-radius: 3px;
    box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
    display: inline-block;
    font-size: var(--jp-ui-font-size0);
    line-height: 1em;
    padding: 0.2em 0.5em;
    }

    /* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
    * At the bottom of cells this is a bit too much as there is also spacing
    * between cells. Going all the way to 0 gets too tight between markdown and
    * code cells.
    */
    .jp-RenderedHTMLCommon > *:last-child {
    margin-bottom: 0.5em;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Copyright (c) 2014-2017, PhosphorJS Contributors
    |
    | Distributed under the terms of the BSD 3-Clause License.
    |
    | The full license is in the file LICENSE, distributed with this software.
    |----------------------------------------------------------------------------*/

    .lm-cursor-backdrop {
    position: fixed;
    width: 200px;
    height: 200px;
    margin-top: -100px;
    margin-left: -100px;
    will-change: transform;
    z-index: 100;
    }

    .lm-mod-drag-image {
    will-change: transform;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    .jp-lineFormSearch {
    padding: 4px 12px;
    background-color: var(--jp-layout-color2);
    box-shadow: var(--jp-toolbar-box-shadow);
    z-index: 2;
    font-size: var(--jp-ui-font-size1);
    }

    .jp-lineFormCaption {
    font-size: var(--jp-ui-font-size0);
    line-height: var(--jp-ui-font-size1);
    margin-top: 4px;
    color: var(--jp-ui-font-color0);
    }

    .jp-baseLineForm {
    border: none;
    border-radius: 0;
    position: absolute;
    background-size: 16px;
    background-repeat: no-repeat;
    background-position: center;
    outline: none;
    }

    .jp-lineFormButtonContainer {
    top: 4px;
    right: 8px;
    height: 24px;
    padding: 0 12px;
    width: 12px;
    }

    .jp-lineFormButtonIcon {
    top: 0;
    right: 0;
    background-color: var(--jp-brand-color1);
    height: 100%;
    width: 100%;
    box-sizing: border-box;
    padding: 4px 6px;
    }

    .jp-lineFormButton {
    top: 0;
    right: 0;
    background-color: transparent;
    height: 100%;
    width: 100%;
    box-sizing: border-box;
    }

    .jp-lineFormWrapper {
    overflow: hidden;
    padding: 0 8px;
    border: 1px solid var(--jp-border-color0);
    background-color: var(--jp-input-active-background);
    height: 22px;
    }

    .jp-lineFormWrapperFocusWithin {
    border: var(--jp-border-width) solid var(--md-blue-500);
    box-shadow: inset 0 0 4px var(--md-blue-300);
    }

    .jp-lineFormInput {
    background: transparent;
    width: 200px;
    height: 100%;
    border: none;
    outline: none;
    color: var(--jp-ui-font-color0);
    line-height: 28px;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) 2014-2016, Jupyter Development Team.
    |
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-JSONEditor {
    display: flex;
    flex-direction: column;
    width: 100%;
    }

    .jp-JSONEditor-host {
    flex: 1 1 auto;
    border: var(--jp-border-width) solid var(--jp-input-border-color);
    border-radius: 0;
    background: var(--jp-layout-color0);
    min-height: 50px;
    padding: 1px;
    }

    .jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
    border-color: red;
    outline-color: red;
    }

    .jp-JSONEditor-header {
    display: flex;
    flex: 1 0 auto;
    padding: 0 0 0 12px;
    }

    .jp-JSONEditor-header label {
    flex: 0 0 auto;
    }

    .jp-JSONEditor-commitButton {
    height: 16px;
    width: 16px;
    background-size: 18px;
    background-repeat: no-repeat;
    background-position: center;
    }

    .jp-JSONEditor-host.jp-mod-focused {
    background-color: var(--jp-input-active-background);
    border: 1px solid var(--jp-input-active-border-color);
    box-shadow: var(--jp-input-box-shadow);
    }

    .jp-Editor.jp-mod-dropTarget {
    border: var(--jp-border-width) solid var(--jp-input-active-border-color);
    box-shadow: var(--jp-input-box-shadow);
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/
    .jp-DocumentSearch-input {
    border: none;
    outline: none;
    color: var(--jp-ui-font-color0);
    font-size: var(--jp-ui-font-size1);
    background-color: var(--jp-layout-color0);
    font-family: var(--jp-ui-font-family);
    padding: 2px 1px;
    resize: none;
    }

    .jp-DocumentSearch-overlay {
    position: absolute;
    background-color: var(--jp-toolbar-background);
    border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
    border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
    top: 0;
    right: 0;
    z-index: 7;
    min-width: 405px;
    padding: 2px;
    font-size: var(--jp-ui-font-size1);

    --jp-private-document-search-button-height: 20px;
    }

    .jp-DocumentSearch-overlay button {
    background-color: var(--jp-toolbar-background);
    outline: 0;
    }

    .jp-DocumentSearch-overlay button:hover {
    background-color: var(--jp-layout-color2);
    }

    .jp-DocumentSearch-overlay button:active {
    background-color: var(--jp-layout-color3);
    }

    .jp-DocumentSearch-overlay-row {
    display: flex;
    align-items: center;
    margin-bottom: 2px;
    }

    .jp-DocumentSearch-button-content {
    display: inline-block;
    cursor: pointer;
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    }

    .jp-DocumentSearch-button-content svg {
    width: 100%;
    height: 100%;
    }

    .jp-DocumentSearch-input-wrapper {
    border: var(--jp-border-width) solid var(--jp-border-color0);
    display: flex;
    background-color: var(--jp-layout-color0);
    margin: 2px;
    }

    .jp-DocumentSearch-input-wrapper:focus-within {
    border-color: var(--jp-cell-editor-active-border-color);
    }

    .jp-DocumentSearch-toggle-wrapper,
    .jp-DocumentSearch-button-wrapper {
    all: initial;
    overflow: hidden;
    display: inline-block;
    border: none;
    box-sizing: border-box;
    }

    .jp-DocumentSearch-toggle-wrapper {
    width: 14px;
    height: 14px;
    }

    .jp-DocumentSearch-button-wrapper {
    width: var(--jp-private-document-search-button-height);
    height: var(--jp-private-document-search-button-height);
    }

    .jp-DocumentSearch-toggle-wrapper:focus,
    .jp-DocumentSearch-button-wrapper:focus {
    outline: var(--jp-border-width) solid
        var(--jp-cell-editor-active-border-color);
    outline-offset: -1px;
    }

    .jp-DocumentSearch-toggle-wrapper,
    .jp-DocumentSearch-button-wrapper,
    .jp-DocumentSearch-button-content:focus {
    outline: none;
    }

    .jp-DocumentSearch-toggle-placeholder {
    width: 5px;
    }

    .jp-DocumentSearch-input-button::before {
    display: block;
    padding-top: 100%;
    }

    .jp-DocumentSearch-input-button-off {
    opacity: var(--jp-search-toggle-off-opacity);
    }

    .jp-DocumentSearch-input-button-off:hover {
    opacity: var(--jp-search-toggle-hover-opacity);
    }

    .jp-DocumentSearch-input-button-on {
    opacity: var(--jp-search-toggle-on-opacity);
    }

    .jp-DocumentSearch-index-counter {
    padding-left: 10px;
    padding-right: 10px;
    user-select: none;
    min-width: 35px;
    display: inline-block;
    }

    .jp-DocumentSearch-up-down-wrapper {
    display: inline-block;
    padding-right: 2px;
    margin-left: auto;
    white-space: nowrap;
    }

    .jp-DocumentSearch-spacer {
    margin-left: auto;
    }

    .jp-DocumentSearch-up-down-wrapper button {
    outline: 0;
    border: none;
    width: var(--jp-private-document-search-button-height);
    height: var(--jp-private-document-search-button-height);
    vertical-align: middle;
    margin: 1px 5px 2px;
    }

    .jp-DocumentSearch-up-down-button:hover {
    background-color: var(--jp-layout-color2);
    }

    .jp-DocumentSearch-up-down-button:active {
    background-color: var(--jp-layout-color3);
    }

    .jp-DocumentSearch-filter-button {
    border-radius: var(--jp-border-radius);
    }

    .jp-DocumentSearch-filter-button:hover {
    background-color: var(--jp-layout-color2);
    }

    .jp-DocumentSearch-filter-button-enabled {
    background-color: var(--jp-layout-color2);
    }

    .jp-DocumentSearch-filter-button-enabled:hover {
    background-color: var(--jp-layout-color3);
    }

    .jp-DocumentSearch-search-options {
    padding: 0 8px;
    margin-left: 3px;
    width: 100%;
    display: grid;
    justify-content: start;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    justify-items: stretch;
    }

    .jp-DocumentSearch-search-filter-disabled {
    color: var(--jp-ui-font-color2);
    }

    .jp-DocumentSearch-search-filter {
    display: flex;
    align-items: center;
    user-select: none;
    }

    .jp-DocumentSearch-regex-error {
    color: var(--jp-error-color0);
    }

    .jp-DocumentSearch-replace-button-wrapper {
    overflow: hidden;
    display: inline-block;
    box-sizing: border-box;
    border: var(--jp-border-width) solid var(--jp-border-color0);
    margin: auto 2px;
    padding: 1px 4px;
    height: calc(var(--jp-private-document-search-button-height) + 2px);
    }

    .jp-DocumentSearch-replace-button-wrapper:focus {
    border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
    }

    .jp-DocumentSearch-replace-button {
    display: inline-block;
    text-align: center;
    cursor: pointer;
    box-sizing: border-box;
    color: var(--jp-ui-font-color1);

    /* height - 2 * (padding of wrapper) */
    line-height: calc(var(--jp-private-document-search-button-height) - 2px);
    width: 100%;
    height: 100%;
    }

    .jp-DocumentSearch-replace-button:focus {
    outline: none;
    }

    .jp-DocumentSearch-replace-wrapper-class {
    margin-left: 14px;
    display: flex;
    }

    .jp-DocumentSearch-replace-toggle {
    border: none;
    background-color: var(--jp-toolbar-background);
    border-radius: var(--jp-border-radius);
    }

    .jp-DocumentSearch-replace-toggle:hover {
    background-color: var(--jp-layout-color2);
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .cm-editor {
    line-height: var(--jp-code-line-height);
    font-size: var(--jp-code-font-size);
    font-family: var(--jp-code-font-family);
    border: 0;
    border-radius: 0;
    height: auto;

    /* Changed to auto to autogrow */
    }

    .cm-editor pre {
    padding: 0 var(--jp-code-padding);
    }

    .jp-CodeMirrorEditor[data-type='inline'] .cm-dialog {
    background-color: var(--jp-layout-color0);
    color: var(--jp-content-font-color1);
    }

    .jp-CodeMirrorEditor {
    cursor: text;
    }

    /* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
    @media screen and (min-width: 2138px) and (max-width: 4319px) {
    .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
        border-left: var(--jp-code-cursor-width1) solid
        var(--jp-editor-cursor-color);
    }
    }

    /* When zoomed out less than 33% */
    @media screen and (min-width: 4320px) {
    .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
        border-left: var(--jp-code-cursor-width2) solid
        var(--jp-editor-cursor-color);
    }
    }

    .cm-editor.jp-mod-readOnly .cm-cursor {
    display: none;
    }

    .jp-CollaboratorCursor {
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: none;
    border-bottom: 3px solid;
    background-clip: content-box;
    margin-left: -5px;
    margin-right: -5px;
    }

    .cm-searching,
    .cm-searching span {
    /* `.cm-searching span`: we need to override syntax highlighting */
    background-color: var(--jp-search-unselected-match-background-color);
    color: var(--jp-search-unselected-match-color);
    }

    .cm-searching::selection,
    .cm-searching span::selection {
    background-color: var(--jp-search-unselected-match-background-color);
    color: var(--jp-search-unselected-match-color);
    }

    .jp-current-match > .cm-searching,
    .jp-current-match > .cm-searching span,
    .cm-searching > .jp-current-match,
    .cm-searching > .jp-current-match span {
    background-color: var(--jp-search-selected-match-background-color);
    color: var(--jp-search-selected-match-color);
    }

    .jp-current-match > .cm-searching::selection,
    .cm-searching > .jp-current-match::selection,
    .jp-current-match > .cm-searching span::selection {
    background-color: var(--jp-search-selected-match-background-color);
    color: var(--jp-search-selected-match-color);
    }

    .cm-trailingspace {
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII=);
    background-position: center left;
    background-repeat: repeat-x;
    }

    .jp-CollaboratorCursor-hover {
    position: absolute;
    z-index: 1;
    transform: translateX(-50%);
    color: white;
    border-radius: 3px;
    padding-left: 4px;
    padding-right: 4px;
    padding-top: 1px;
    padding-bottom: 1px;
    text-align: center;
    font-size: var(--jp-ui-font-size1);
    white-space: nowrap;
    }

    .jp-CodeMirror-ruler {
    border-left: 1px dashed var(--jp-border-color2);
    }

    /* Styles for shared cursors (remote cursor locations and selected ranges) */
    .jp-CodeMirrorEditor .cm-ySelectionCaret {
    position: relative;
    border-left: 1px solid black;
    margin-left: -1px;
    margin-right: -1px;
    box-sizing: border-box;
    }

    .jp-CodeMirrorEditor .cm-ySelectionCaret > .cm-ySelectionInfo {
    white-space: nowrap;
    position: absolute;
    top: -1.15em;
    padding-bottom: 0.05em;
    left: -1px;
    font-size: 0.95em;
    font-family: var(--jp-ui-font-family);
    font-weight: bold;
    line-height: normal;
    user-select: none;
    color: white;
    padding-left: 2px;
    padding-right: 2px;
    z-index: 101;
    transition: opacity 0.3s ease-in-out;
    }

    .jp-CodeMirrorEditor .cm-ySelectionInfo {
    transition-delay: 0.7s;
    opacity: 0;
    }

    .jp-CodeMirrorEditor .cm-ySelectionCaret:hover > .cm-ySelectionInfo {
    opacity: 1;
    transition-delay: 0s;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-MimeDocument {
    outline: none;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Variables
    |----------------------------------------------------------------------------*/

    :root {
    --jp-private-filebrowser-button-height: 28px;
    --jp-private-filebrowser-button-width: 48px;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-FileBrowser .jp-SidePanel-content {
    display: flex;
    flex-direction: column;
    }

    .jp-FileBrowser-toolbar.jp-Toolbar {
    flex-wrap: wrap;
    row-gap: 12px;
    border-bottom: none;
    height: auto;
    margin: 8px 12px 0;
    box-shadow: none;
    padding: 0;
    justify-content: flex-start;
    }

    .jp-FileBrowser-Panel {
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    }

    .jp-BreadCrumbs {
    flex: 0 0 auto;
    margin: 8px 12px;
    }

    .jp-BreadCrumbs-item {
    margin: 0 2px;
    padding: 0 2px;
    border-radius: var(--jp-border-radius);
    cursor: pointer;
    }

    .jp-BreadCrumbs-item:hover {
    background-color: var(--jp-layout-color2);
    }

    .jp-BreadCrumbs-item:first-child {
    margin-left: 0;
    }

    .jp-BreadCrumbs-item.jp-mod-dropTarget {
    background-color: var(--jp-brand-color2);
    opacity: 0.7;
    }

    /*-----------------------------------------------------------------------------
    | Buttons
    |----------------------------------------------------------------------------*/

    .jp-FileBrowser-toolbar > .jp-Toolbar-item {
    flex: 0 0 auto;
    padding-left: 0;
    padding-right: 2px;
    align-items: center;
    height: unset;
    }

    .jp-FileBrowser-toolbar > .jp-Toolbar-item .jp-ToolbarButtonComponent {
    width: 40px;
    }

    /*-----------------------------------------------------------------------------
    | Other styles
    |----------------------------------------------------------------------------*/

    .jp-FileDialog.jp-mod-conflict input {
    color: var(--jp-error-color1);
    }

    .jp-FileDialog .jp-new-name-title {
    margin-top: 12px;
    }

    .jp-LastModified-hidden {
    display: none;
    }

    .jp-FileSize-hidden {
    display: none;
    }

    .jp-FileBrowser .lm-AccordionPanel > h3:first-child {
    display: none;
    }

    /*-----------------------------------------------------------------------------
    | DirListing
    |----------------------------------------------------------------------------*/

    .jp-DirListing {
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    outline: 0;
    }

    .jp-DirListing-header {
    flex: 0 0 auto;
    display: flex;
    flex-direction: row;
    align-items: center;
    overflow: hidden;
    border-top: var(--jp-border-width) solid var(--jp-border-color2);
    border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
    box-shadow: var(--jp-toolbar-box-shadow);
    z-index: 2;
    }

    .jp-DirListing-headerItem {
    padding: 4px 12px 2px;
    font-weight: 500;
    }

    .jp-DirListing-headerItem:hover {
    background: var(--jp-layout-color2);
    }

    .jp-DirListing-headerItem.jp-id-name {
    flex: 1 0 84px;
    }

    .jp-DirListing-headerItem.jp-id-modified {
    flex: 0 0 112px;
    border-left: var(--jp-border-width) solid var(--jp-border-color2);
    text-align: right;
    }

    .jp-DirListing-headerItem.jp-id-filesize {
    flex: 0 0 75px;
    border-left: var(--jp-border-width) solid var(--jp-border-color2);
    text-align: right;
    }

    .jp-id-narrow {
    display: none;
    flex: 0 0 5px;
    padding: 4px;
    border-left: var(--jp-border-width) solid var(--jp-border-color2);
    text-align: right;
    color: var(--jp-border-color2);
    }

    .jp-DirListing-narrow .jp-id-narrow {
    display: block;
    }

    .jp-DirListing-narrow .jp-id-modified,
    .jp-DirListing-narrow .jp-DirListing-itemModified {
    display: none;
    }

    .jp-DirListing-headerItem.jp-mod-selected {
    font-weight: 600;
    }

    /* increase specificity to override bundled default */
    .jp-DirListing-content {
    flex: 1 1 auto;
    margin: 0;
    padding: 0;
    list-style-type: none;
    overflow: auto;
    background-color: var(--jp-layout-color1);
    }

    .jp-DirListing-content mark {
    color: var(--jp-ui-font-color0);
    background-color: transparent;
    font-weight: bold;
    }

    .jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
    color: var(--jp-ui-inverse-font-color0);
    }

    /* Style the directory listing content when a user drops a file to upload */
    .jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
    outline: 5px dashed rgba(128, 128, 128, 0.5);
    outline-offset: -10px;
    cursor: copy;
    }

    .jp-DirListing-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 4px 12px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    .jp-DirListing-checkboxWrapper {
    /* Increases hit area of checkbox. */
    padding: 4px;
    }

    .jp-DirListing-header
    .jp-DirListing-checkboxWrapper
    + .jp-DirListing-headerItem {
    padding-left: 4px;
    }

    .jp-DirListing-content .jp-DirListing-checkboxWrapper {
    position: relative;
    left: -4px;
    margin: -4px 0 -4px -8px;
    }

    .jp-DirListing-checkboxWrapper.jp-mod-visible {
    visibility: visible;
    }

    /* For devices that support hovering, hide checkboxes until hovered, selected...
    */
    @media (hover: hover) {
    .jp-DirListing-checkboxWrapper {
        visibility: hidden;
    }

    .jp-DirListing-item:hover .jp-DirListing-checkboxWrapper,
    .jp-DirListing-item.jp-mod-selected .jp-DirListing-checkboxWrapper {
        visibility: visible;
    }
    }

    .jp-DirListing-item[data-is-dot] {
    opacity: 75%;
    }

    .jp-DirListing-item.jp-mod-selected {
    color: var(--jp-ui-inverse-font-color1);
    background: var(--jp-brand-color1);
    }

    .jp-DirListing-item.jp-mod-dropTarget {
    background: var(--jp-brand-color3);
    }

    .jp-DirListing-item:hover:not(.jp-mod-selected) {
    background: var(--jp-layout-color2);
    }

    .jp-DirListing-itemIcon {
    flex: 0 0 20px;
    margin-right: 4px;
    }

    .jp-DirListing-itemText {
    flex: 1 0 64px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    user-select: none;
    }

    .jp-DirListing-itemText:focus {
    outline-width: 2px;
    outline-color: var(--jp-inverse-layout-color1);
    outline-style: solid;
    outline-offset: 1px;
    }

    .jp-DirListing-item.jp-mod-selected .jp-DirListing-itemText:focus {
    outline-color: var(--jp-layout-color1);
    }

    .jp-DirListing-itemModified {
    flex: 0 0 125px;
    text-align: right;
    }

    .jp-DirListing-itemFileSize {
    flex: 0 0 90px;
    text-align: right;
    }

    .jp-DirListing-editor {
    flex: 1 0 64px;
    outline: none;
    border: none;
    color: var(--jp-ui-font-color1);
    background-color: var(--jp-layout-color1);
    }

    .jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon::before {
    color: var(--jp-success-color1);
    content: '\25CF';
    font-size: 8px;
    position: absolute;
    left: -8px;
    }

    .jp-DirListing-item.jp-mod-running.jp-mod-selected
    .jp-DirListing-itemIcon::before {
    color: var(--jp-ui-inverse-font-color1);
    }

    .jp-DirListing-item.lm-mod-drag-image,
    .jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
    font-size: var(--jp-ui-font-size1);
    padding-left: 4px;
    margin-left: 4px;
    width: 160px;
    background-color: var(--jp-ui-inverse-font-color2);
    box-shadow: var(--jp-elevation-z2);
    border-radius: 0;
    color: var(--jp-ui-font-color1);
    transform: translateX(-40%) translateY(-58%);
    }

    .jp-Document {
    min-width: 120px;
    min-height: 120px;
    outline: none;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Main OutputArea
    | OutputArea has a list of Outputs
    |----------------------------------------------------------------------------*/

    .jp-OutputArea {
    overflow-y: auto;
    }

    .jp-OutputArea-child {
    display: table;
    table-layout: fixed;
    width: 100%;
    overflow: hidden;
    }

    .jp-OutputPrompt {
    width: var(--jp-cell-prompt-width);
    color: var(--jp-cell-outprompt-font-color);
    font-family: var(--jp-cell-prompt-font-family);
    padding: var(--jp-code-padding);
    letter-spacing: var(--jp-cell-prompt-letter-spacing);
    line-height: var(--jp-code-line-height);
    font-size: var(--jp-code-font-size);
    border: var(--jp-border-width) solid transparent;
    opacity: var(--jp-cell-prompt-opacity);

    /* Right align prompt text, don't wrap to handle large prompt numbers */
    text-align: right;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

    /* Disable text selection */
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    .jp-OutputArea-prompt {
    display: table-cell;
    vertical-align: top;
    }

    .jp-OutputArea-output {
    display: table-cell;
    width: 100%;
    height: auto;
    overflow: auto;
    user-select: text;
    -moz-user-select: text;
    -webkit-user-select: text;
    -ms-user-select: text;
    }

    .jp-OutputArea .jp-RenderedText {
    padding-left: 1ch;
    }

    /**
    * Prompt overlay.
    */

    .jp-OutputArea-promptOverlay {
    position: absolute;
    top: 0;
    width: var(--jp-cell-prompt-width);
    height: 100%;
    opacity: 0.5;
    }

    .jp-OutputArea-promptOverlay:hover {
    background: var(--jp-layout-color2);
    box-shadow: inset 0 0 1px var(--jp-inverse-layout-color0);
    cursor: zoom-out;
    }

    .jp-mod-outputsScrolled .jp-OutputArea-promptOverlay:hover {
    cursor: zoom-in;
    }

    /**
    * Isolated output.
    */
    .jp-OutputArea-output.jp-mod-isolated {
    width: 100%;
    display: block;
    }

    /*
    When drag events occur, `lm-mod-override-cursor` is added to the body.
    Because iframes steal all cursor events, the following two rules are necessary
    to suppress pointer events while resize drags are occurring. There may be a
    better solution to this problem.
    */
    body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
    position: relative;
    }

    body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: transparent;
    }

    /* pre */

    .jp-OutputArea-output pre {
    border: none;
    margin: 0;
    padding: 0;
    overflow-x: auto;
    overflow-y: auto;
    word-break: break-all;
    word-wrap: break-word;
    white-space: pre-wrap;
    }

    /* tables */

    .jp-OutputArea-output.jp-RenderedHTMLCommon table {
    margin-left: 0;
    margin-right: 0;
    }

    /* description lists */

    .jp-OutputArea-output dl,
    .jp-OutputArea-output dt,
    .jp-OutputArea-output dd {
    display: block;
    }

    .jp-OutputArea-output dl {
    width: 100%;
    overflow: hidden;
    padding: 0;
    margin: 0;
    }

    .jp-OutputArea-output dt {
    font-weight: bold;
    float: left;
    width: 20%;
    padding: 0;
    margin: 0;
    }

    .jp-OutputArea-output dd {
    float: left;
    width: 80%;
    padding: 0;
    margin: 0;
    }

    .jp-TrimmedOutputs pre {
    background: var(--jp-layout-color3);
    font-size: calc(var(--jp-code-font-size) * 1.4);
    text-align: center;
    text-transform: uppercase;
    }

    /* Hide the gutter in case of
    *  - nested output areas (e.g. in the case of output widgets)
    *  - mirrored output areas
    */
    .jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
    display: none;
    }

    /* Hide empty lines in the output area, for instance due to cleared widgets */
    .jp-OutputArea-prompt:empty {
    padding: 0;
    border: 0;
    }

    /*-----------------------------------------------------------------------------
    | executeResult is added to any Output-result for the display of the object
    | returned by a cell
    |----------------------------------------------------------------------------*/

    .jp-OutputArea-output.jp-OutputArea-executeResult {
    margin-left: 0;
    width: 100%;
    }

    /* Text output with the Out[] prompt needs a top padding to match the
    * alignment of the Out[] prompt itself.
    */
    .jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
    padding-top: var(--jp-code-padding);
    border-top: var(--jp-border-width) solid transparent;
    }

    /*-----------------------------------------------------------------------------
    | The Stdin output
    |----------------------------------------------------------------------------*/

    .jp-Stdin-prompt {
    color: var(--jp-content-font-color0);
    padding-right: var(--jp-code-padding);
    vertical-align: baseline;
    flex: 0 0 auto;
    }

    .jp-Stdin-input {
    font-family: var(--jp-code-font-family);
    font-size: inherit;
    color: inherit;
    background-color: inherit;
    width: 42%;
    min-width: 200px;

    /* make sure input baseline aligns with prompt */
    vertical-align: baseline;

    /* padding + margin = 0.5em between prompt and cursor */
    padding: 0 0.25em;
    margin: 0 0.25em;
    flex: 0 0 70%;
    }

    .jp-Stdin-input::placeholder {
    opacity: 0;
    }

    .jp-Stdin-input:focus {
    box-shadow: none;
    }

    .jp-Stdin-input:focus::placeholder {
    opacity: 1;
    }

    /*-----------------------------------------------------------------------------
    | Output Area View
    |----------------------------------------------------------------------------*/

    .jp-LinkedOutputView .jp-OutputArea {
    height: 100%;
    display: block;
    }

    .jp-LinkedOutputView .jp-OutputArea-output:only-child {
    height: 100%;
    }

    /*-----------------------------------------------------------------------------
    | Printing
    |----------------------------------------------------------------------------*/

    @media print {
    .jp-OutputArea-child {
        break-inside: avoid-page;
    }
    }

    /*-----------------------------------------------------------------------------
    | Mobile
    |----------------------------------------------------------------------------*/
    @media only screen and (max-width: 760px) {
    .jp-OutputPrompt {
        display: table-row;
        text-align: left;
    }

    .jp-OutputArea-child .jp-OutputArea-output {
        display: table-row;
        margin-left: var(--jp-notebook-padding);
    }
    }

    /* Trimmed outputs warning */
    .jp-TrimmedOutputs > a {
    margin: 10px;
    text-decoration: none;
    cursor: pointer;
    }

    .jp-TrimmedOutputs > a:hover {
    text-decoration: none;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Table of Contents
    |----------------------------------------------------------------------------*/

    :root {
    --jp-private-toc-active-width: 4px;
    }

    .jp-TableOfContents {
    display: flex;
    flex-direction: column;
    background: var(--jp-layout-color1);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    height: 100%;
    }

    .jp-TableOfContents-placeholder {
    text-align: center;
    }

    .jp-TableOfContents-placeholderContent {
    color: var(--jp-content-font-color2);
    padding: 8px;
    }

    .jp-TableOfContents-placeholderContent > h3 {
    margin-bottom: var(--jp-content-heading-margin-bottom);
    }

    .jp-TableOfContents .jp-SidePanel-content {
    overflow-y: auto;
    }

    .jp-TableOfContents-tree {
    margin: 4px;
    }

    .jp-TableOfContents ol {
    list-style-type: none;
    }

    /* stylelint-disable-next-line selector-max-type */
    .jp-TableOfContents li > ol {
    /* Align left border with triangle icon center */
    padding-left: 11px;
    }

    .jp-TableOfContents-content {
    /* left margin for the active heading indicator */
    margin: 0 0 0 var(--jp-private-toc-active-width);
    padding: 0;
    background-color: var(--jp-layout-color1);
    }

    .jp-tocItem {
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    .jp-tocItem-heading {
    display: flex;
    cursor: pointer;
    }

    .jp-tocItem-heading:hover {
    background-color: var(--jp-layout-color2);
    }

    .jp-tocItem-content {
    display: block;
    padding: 4px 0;
    white-space: nowrap;
    text-overflow: ellipsis;
    overflow-x: hidden;
    }

    .jp-tocItem-collapser {
    height: 20px;
    margin: 2px 2px 0;
    padding: 0;
    background: none;
    border: none;
    cursor: pointer;
    }

    .jp-tocItem-collapser:hover {
    background-color: var(--jp-layout-color3);
    }

    /* Active heading indicator */

    .jp-tocItem-heading::before {
    content: ' ';
    background: transparent;
    width: var(--jp-private-toc-active-width);
    height: 24px;
    position: absolute;
    left: 0;
    border-radius: var(--jp-border-radius);
    }

    .jp-tocItem-heading.jp-tocItem-active::before {
    background-color: var(--jp-brand-color1);
    }

    .jp-tocItem-heading:hover.jp-tocItem-active::before {
    background: var(--jp-brand-color0);
    opacity: 1;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    .jp-Collapser {
    flex: 0 0 var(--jp-cell-collapser-width);
    padding: 0;
    margin: 0;
    border: none;
    outline: none;
    background: transparent;
    border-radius: var(--jp-border-radius);
    opacity: 1;
    }

    .jp-Collapser-child {
    display: block;
    width: 100%;
    box-sizing: border-box;

    /* height: 100% doesn't work because the height of its parent is computed from content */
    position: absolute;
    top: 0;
    bottom: 0;
    }

    /*-----------------------------------------------------------------------------
    | Printing
    |----------------------------------------------------------------------------*/

    /*
    Hiding collapsers in print mode.

    Note: input and output wrappers have "display: block" propery in print mode.
    */

    @media print {
    .jp-Collapser {
        display: none;
    }
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Header/Footer
    |----------------------------------------------------------------------------*/

    /* Hidden by zero height by default */
    .jp-CellHeader,
    .jp-CellFooter {
    height: 0;
    width: 100%;
    padding: 0;
    margin: 0;
    border: none;
    outline: none;
    background: transparent;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Input
    |----------------------------------------------------------------------------*/

    /* All input areas */
    .jp-InputArea {
    display: table;
    table-layout: fixed;
    width: 100%;
    overflow: hidden;
    }

    .jp-InputArea-editor {
    display: table-cell;
    overflow: hidden;
    vertical-align: top;

    /* This is the non-active, default styling */
    border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
    border-radius: 0;
    background: var(--jp-cell-editor-background);
    }

    .jp-InputPrompt {
    display: table-cell;
    vertical-align: top;
    width: var(--jp-cell-prompt-width);
    color: var(--jp-cell-inprompt-font-color);
    font-family: var(--jp-cell-prompt-font-family);
    padding: var(--jp-code-padding);
    letter-spacing: var(--jp-cell-prompt-letter-spacing);
    opacity: var(--jp-cell-prompt-opacity);
    line-height: var(--jp-code-line-height);
    font-size: var(--jp-code-font-size);
    border: var(--jp-border-width) solid transparent;

    /* Right align prompt text, don't wrap to handle large prompt numbers */
    text-align: right;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

    /* Disable text selection */
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    }

    /*-----------------------------------------------------------------------------
    | Mobile
    |----------------------------------------------------------------------------*/
    @media only screen and (max-width: 760px) {
    .jp-InputArea-editor {
        display: table-row;
        margin-left: var(--jp-notebook-padding);
    }

    .jp-InputPrompt {
        display: table-row;
        text-align: left;
    }
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Placeholder
    |----------------------------------------------------------------------------*/

    .jp-Placeholder {
    display: table;
    table-layout: fixed;
    width: 100%;
    }

    .jp-Placeholder-prompt {
    display: table-cell;
    box-sizing: border-box;
    }

    .jp-Placeholder-content {
    display: table-cell;
    padding: 4px 6px;
    border: 1px solid transparent;
    border-radius: 0;
    background: none;
    box-sizing: border-box;
    cursor: pointer;
    }

    .jp-Placeholder-contentContainer {
    display: flex;
    }

    .jp-Placeholder-content:hover,
    .jp-InputPlaceholder > .jp-Placeholder-content:hover {
    border-color: var(--jp-layout-color3);
    }

    .jp-Placeholder-content .jp-MoreHorizIcon {
    width: 32px;
    height: 16px;
    border: 1px solid transparent;
    border-radius: var(--jp-border-radius);
    }

    .jp-Placeholder-content .jp-MoreHorizIcon:hover {
    border: 1px solid var(--jp-border-color1);
    box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.25);
    background-color: var(--jp-layout-color0);
    }

    .jp-PlaceholderText {
    white-space: nowrap;
    overflow-x: hidden;
    color: var(--jp-inverse-layout-color3);
    font-family: var(--jp-code-font-family);
    }

    .jp-InputPlaceholder > .jp-Placeholder-content {
    border-color: var(--jp-cell-editor-border-color);
    background: var(--jp-cell-editor-background);
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Private CSS variables
    |----------------------------------------------------------------------------*/

    :root {
    --jp-private-cell-scrolling-output-offset: 5px;
    }

    /*-----------------------------------------------------------------------------
    | Cell
    |----------------------------------------------------------------------------*/

    .jp-Cell {
    padding: var(--jp-cell-padding);
    margin: 0;
    border: none;
    outline: none;
    background: transparent;
    }

    /*-----------------------------------------------------------------------------
    | Common input/output
    |----------------------------------------------------------------------------*/

    .jp-Cell-inputWrapper,
    .jp-Cell-outputWrapper {
    display: flex;
    flex-direction: row;
    padding: 0;
    margin: 0;

    /* Added to reveal the box-shadow on the input and output collapsers. */
    overflow: visible;
    }

    /* Only input/output areas inside cells */
    .jp-Cell-inputArea,
    .jp-Cell-outputArea {
    flex: 1 1 auto;
    }

    /*-----------------------------------------------------------------------------
    | Collapser
    |----------------------------------------------------------------------------*/

    /* Make the output collapser disappear when there is not output, but do so
    * in a manner that leaves it in the layout and preserves its width.
    */
    .jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
    border: none !important;
    background: transparent !important;
    }

    .jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
    min-height: var(--jp-cell-collapser-min-height);
    }

    /*-----------------------------------------------------------------------------
    | Output
    |----------------------------------------------------------------------------*/

    /* Put a space between input and output when there IS output */
    .jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
    margin-top: 5px;
    }

    .jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
    overflow-y: auto;
    max-height: 24em;
    margin-left: var(--jp-private-cell-scrolling-output-offset);
    resize: vertical;
    }

    .jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea[style*='height'] {
    max-height: unset;
    }

    .jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea::after {
    content: ' ';
    box-shadow: inset 0 0 6px 2px rgb(0 0 0 / 30%);
    width: 100%;
    height: 100%;
    position: sticky;
    bottom: 0;
    top: 0;
    margin-top: -50%;
    float: left;
    display: block;
    pointer-events: none;
    }

    .jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-child {
    padding-top: 6px;
    }

    .jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
    width: calc(
        var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
    );
    }

    .jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay {
    left: calc(-1 * var(--jp-private-cell-scrolling-output-offset));
    }

    /*-----------------------------------------------------------------------------
    | CodeCell
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | MarkdownCell
    |----------------------------------------------------------------------------*/

    .jp-MarkdownOutput {
    display: table-cell;
    width: 100%;
    margin-top: 0;
    margin-bottom: 0;
    padding-left: var(--jp-code-padding);
    }

    .jp-MarkdownOutput.jp-RenderedHTMLCommon {
    overflow: auto;
    }

    /* collapseHeadingButton (show always if hiddenCellsButton is _not_ shown) */
    .jp-collapseHeadingButton {
    display: flex;
    min-height: var(--jp-cell-collapser-min-height);
    font-size: var(--jp-code-font-size);
    position: absolute;
    background-color: transparent;
    background-size: 25px;
    background-repeat: no-repeat;
    background-position-x: center;
    background-position-y: top;
    background-image: var(--jp-icon-caret-down);
    right: 0;
    top: 0;
    bottom: 0;
    }

    .jp-collapseHeadingButton.jp-mod-collapsed {
    background-image: var(--jp-icon-caret-right);
    }

    /*
    set the container font size to match that of content
    so that the nested collapse buttons have the right size
    */
    .jp-MarkdownCell .jp-InputPrompt {
    font-size: var(--jp-content-font-size1);
    }

    /*
    Align collapseHeadingButton with cell top header
    The font sizes are identical to the ones in packages/rendermime/style/base.css
    */
    .jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='1'] {
    font-size: var(--jp-content-font-size5);
    background-position-y: calc(0.3 * var(--jp-content-font-size5));
    }

    .jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='2'] {
    font-size: var(--jp-content-font-size4);
    background-position-y: calc(0.3 * var(--jp-content-font-size4));
    }

    .jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='3'] {
    font-size: var(--jp-content-font-size3);
    background-position-y: calc(0.3 * var(--jp-content-font-size3));
    }

    .jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='4'] {
    font-size: var(--jp-content-font-size2);
    background-position-y: calc(0.3 * var(--jp-content-font-size2));
    }

    .jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='5'] {
    font-size: var(--jp-content-font-size1);
    background-position-y: top;
    }

    .jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='6'] {
    font-size: var(--jp-content-font-size0);
    background-position-y: top;
    }

    /* collapseHeadingButton (show only on (hover,active) if hiddenCellsButton is shown) */
    .jp-Notebook.jp-mod-showHiddenCellsButton .jp-collapseHeadingButton {
    display: none;
    }

    .jp-Notebook.jp-mod-showHiddenCellsButton
    :is(.jp-MarkdownCell:hover, .jp-mod-active)
    .jp-collapseHeadingButton {
    display: flex;
    }

    /* showHiddenCellsButton (only show if jp-mod-showHiddenCellsButton is set, which
    is a consequence of the showHiddenCellsButton option in Notebook Settings)*/
    .jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton {
    margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
    margin-top: var(--jp-code-padding);
    border: 1px solid var(--jp-border-color2);
    background-color: var(--jp-border-color3) !important;
    color: var(--jp-content-font-color0) !important;
    display: flex;
    }

    .jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton:hover {
    background-color: var(--jp-border-color2) !important;
    }

    .jp-showHiddenCellsButton {
    display: none;
    }

    /*-----------------------------------------------------------------------------
    | Printing
    |----------------------------------------------------------------------------*/

    /*
    Using block instead of flex to allow the use of the break-inside CSS property for
    cell outputs.
    */

    @media print {
    .jp-Cell-inputWrapper,
    .jp-Cell-outputWrapper {
        display: block;
    }
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Variables
    |----------------------------------------------------------------------------*/

    :root {
    --jp-notebook-toolbar-padding: 2px 5px 2px 2px;
    }

    /*-----------------------------------------------------------------------------

    /*-----------------------------------------------------------------------------
    | Styles
    |----------------------------------------------------------------------------*/

    .jp-NotebookPanel-toolbar {
    padding: var(--jp-notebook-toolbar-padding);

    /* disable paint containment from lumino 2.0 default strict CSS containment */
    contain: style size !important;
    }

    .jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
    border: none;
    box-shadow: none;
    }

    .jp-Notebook-toolbarCellTypeDropdown select {
    height: 24px;
    font-size: var(--jp-ui-font-size1);
    line-height: 14px;
    border-radius: 0;
    display: block;
    }

    .jp-Notebook-toolbarCellTypeDropdown span {
    top: 5px !important;
    }

    .jp-Toolbar-responsive-popup {
    position: absolute;
    height: fit-content;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: flex-end;
    border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
    box-shadow: var(--jp-toolbar-box-shadow);
    background: var(--jp-toolbar-background);
    min-height: var(--jp-toolbar-micro-height);
    padding: var(--jp-notebook-toolbar-padding);
    z-index: 1;
    right: 0;
    top: 0;
    }

    .jp-Toolbar > .jp-Toolbar-responsive-opener {
    margin-left: auto;
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Variables
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------

    /*-----------------------------------------------------------------------------
    | Styles
    |----------------------------------------------------------------------------*/

    .jp-Notebook-ExecutionIndicator {
    position: relative;
    display: inline-block;
    height: 100%;
    z-index: 9997;
    }

    .jp-Notebook-ExecutionIndicator-tooltip {
    visibility: hidden;
    height: auto;
    width: max-content;
    width: -moz-max-content;
    background-color: var(--jp-layout-color2);
    color: var(--jp-ui-font-color1);
    text-align: justify;
    border-radius: 6px;
    padding: 0 5px;
    position: fixed;
    display: table;
    }

    .jp-Notebook-ExecutionIndicator-tooltip.up {
    transform: translateX(-50%) translateY(-100%) translateY(-32px);
    }

    .jp-Notebook-ExecutionIndicator-tooltip.down {
    transform: translateX(calc(-100% + 16px)) translateY(5px);
    }

    .jp-Notebook-ExecutionIndicator-tooltip.hidden {
    display: none;
    }

    .jp-Notebook-ExecutionIndicator:hover .jp-Notebook-ExecutionIndicator-tooltip {
    visibility: visible;
    }

    .jp-Notebook-ExecutionIndicator span {
    font-size: var(--jp-ui-font-size1);
    font-family: var(--jp-ui-font-family);
    color: var(--jp-ui-font-color1);
    line-height: 24px;
    display: block;
    }

    .jp-Notebook-ExecutionIndicator-progress-bar {
    display: flex;
    justify-content: center;
    height: 100%;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    /*
    * Execution indicator
    */
    .jp-tocItem-content::after {
    content: '';

    /* Must be identical to form a circle */
    width: 12px;
    height: 12px;
    background: none;
    border: none;
    position: absolute;
    right: 0;
    }

    .jp-tocItem-content[data-running='0']::after {
    border-radius: 50%;
    border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
    background: none;
    }

    .jp-tocItem-content[data-running='1']::after {
    border-radius: 50%;
    border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
    background-color: var(--jp-inverse-layout-color3);
    }

    .jp-tocItem-content[data-running='0'],
    .jp-tocItem-content[data-running='1'] {
    margin-right: 12px;
    }

    /*
    * Copyright (c) Jupyter Development Team.
    * Distributed under the terms of the Modified BSD License.
    */

    .jp-Notebook-footer {
    height: 27px;
    margin-left: calc(
        var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
        var(--jp-cell-padding)
    );
    width: calc(
        100% -
        (
            var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
            var(--jp-cell-padding) + var(--jp-cell-padding)
        )
    );
    border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
    color: var(--jp-ui-font-color3);
    margin-top: 6px;
    background: none;
    cursor: pointer;
    }

    .jp-Notebook-footer:focus {
    border-color: var(--jp-cell-editor-active-border-color);
    }

    /* For devices that support hovering, hide footer until hover */
    @media (hover: hover) {
    .jp-Notebook-footer {
        opacity: 0;
    }

    .jp-Notebook-footer:focus,
    .jp-Notebook-footer:hover {
        opacity: 1;
    }
    }

    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | Imports
    |----------------------------------------------------------------------------*/

    /*-----------------------------------------------------------------------------
    | CSS variables
    |----------------------------------------------------------------------------*/

    :root {
    --jp-side-by-side-output-size: 1fr;
    --jp-side-by-side-resized-cell: var(--jp-side-by-side-output-size);
    --jp-private-notebook-dragImage-width: 304px;
    --jp-private-notebook-dragImage-height: 36px;
    --jp-private-notebook-selected-color: var(--md-blue-400);
    --jp-private-notebook-active-color: var(--md-green-400);
    }

    /*-----------------------------------------------------------------------------
    | Notebook
    |----------------------------------------------------------------------------*/

    /* stylelint-disable selector-max-class */

    .jp-NotebookPanel {
    display: block;
    height: 100%;
    }

    .jp-NotebookPanel.jp-Document {
    min-width: 240px;
    min-height: 120px;
    }

    .jp-Notebook {
    padding: var(--jp-notebook-padding);
    outline: none;
    overflow: auto;
    background: var(--jp-layout-color0);
    }

    .jp-Notebook.jp-mod-scrollPastEnd::after {
    display: block;
    content: '';
    min-height: var(--jp-notebook-scroll-padding);
    }

    .jp-MainAreaWidget-ContainStrict .jp-Notebook * {
    contain: strict;
    }

    .jp-Notebook .jp-Cell {
    overflow: visible;
    }

    .jp-Notebook .jp-Cell .jp-InputPrompt {
    cursor: move;
    }

    /*-----------------------------------------------------------------------------
    | Notebook state related styling
    |
    | The notebook and cells each have states, here are the possibilities:
    |
    | - Notebook
    |   - Command
    |   - Edit
    | - Cell
    |   - None
    |   - Active (only one can be active)
    |   - Selected (the cells actions are applied to)
    |   - Multiselected (when multiple selected, the cursor)
    |   - No outputs
    |----------------------------------------------------------------------------*/

    /* Command or edit modes */

    .jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
    opacity: var(--jp-cell-prompt-not-active-opacity);
    color: var(--jp-cell-prompt-not-active-font-color);
    }

    .jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
    opacity: var(--jp-cell-prompt-not-active-opacity);
    color: var(--jp-cell-prompt-not-active-font-color);
    }

    /* cell is active */
    .jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
    background: var(--jp-brand-color1);
    }

    /* cell is dirty */
    .jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
    color: var(--jp-warn-color1);
    }

    .jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt::before {
    color: var(--jp-warn-color1);
    content: '•';
    }

    .jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
    background: var(--jp-warn-color1);
    }

    /* collapser is hovered */
    .jp-Notebook .jp-Cell .jp-Collapser:hover {
    box-shadow: var(--jp-elevation-z2);
    background: var(--jp-brand-color1);
    opacity: var(--jp-cell-collapser-not-active-hover-opacity);
    }

    /* cell is active and collapser is hovered */
    .jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
    background: var(--jp-brand-color0);
    opacity: 1;
    }

    /* Command mode */

    .jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
    background: var(--jp-notebook-multiselected-color);
    }

    .jp-Notebook.jp-mod-commandMode
    .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
    background: transparent;
    }

    /* Edit mode */

    .jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
    border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
    box-shadow: var(--jp-input-box-shadow);
    background-color: var(--jp-cell-editor-active-background);
    }

    /*-----------------------------------------------------------------------------
    | Notebook drag and drop
    |----------------------------------------------------------------------------*/

    .jp-Notebook-cell.jp-mod-dropSource {
    opacity: 0.5;
    }

    .jp-Notebook-cell.jp-mod-dropTarget,
    .jp-Notebook.jp-mod-commandMode
    .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
    border-top-color: var(--jp-private-notebook-selected-color);
    border-top-style: solid;
    border-top-width: 2px;
    }

    .jp-dragImage {
    display: block;
    flex-direction: row;
    width: var(--jp-private-notebook-dragImage-width);
    height: var(--jp-private-notebook-dragImage-height);
    border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
    background: var(--jp-cell-editor-background);
    overflow: visible;
    }

    .jp-dragImage-singlePrompt {
    box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
    }

    .jp-dragImage .jp-dragImage-content {
    flex: 1 1 auto;
    z-index: 2;
    font-size: var(--jp-code-font-size);
    font-family: var(--jp-code-font-family);
    line-height: var(--jp-code-line-height);
    padding: var(--jp-code-padding);
    border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
    background: var(--jp-cell-editor-background-color);
    color: var(--jp-content-font-color3);
    text-align: left;
    margin: 4px 4px 4px 0;
    }

    .jp-dragImage .jp-dragImage-prompt {
    flex: 0 0 auto;
    min-width: 36px;
    color: var(--jp-cell-inprompt-font-color);
    padding: var(--jp-code-padding);
    padding-left: 12px;
    font-family: var(--jp-cell-prompt-font-family);
    letter-spacing: var(--jp-cell-prompt-letter-spacing);
    line-height: 1.9;
    font-size: var(--jp-code-font-size);
    border: var(--jp-border-width) solid transparent;
    }

    .jp-dragImage-multipleBack {
    z-index: -1;
    position: absolute;
    height: 32px;
    width: 300px;
    top: 8px;
    left: 8px;
    background: var(--jp-layout-color2);
    border: var(--jp-border-width) solid var(--jp-input-border-color);
    box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
    }

    /*-----------------------------------------------------------------------------
    | Cell toolbar
    |----------------------------------------------------------------------------*/

    .jp-NotebookTools {
    display: block;
    min-width: var(--jp-sidebar-min-width);
    color: var(--jp-ui-font-color1);
    background: var(--jp-layout-color1);

    /* This is needed so that all font sizing of children done in ems is
        * relative to this base size */
    font-size: var(--jp-ui-font-size1);
    overflow: auto;
    }

    .jp-ActiveCellTool {
    padding: 12px 0;
    display: flex;
    }

    .jp-ActiveCellTool-Content {
    flex: 1 1 auto;
    }

    .jp-ActiveCellTool .jp-ActiveCellTool-CellContent {
    background: var(--jp-cell-editor-background);
    border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
    border-radius: 0;
    min-height: 29px;
    }

    .jp-ActiveCellTool .jp-InputPrompt {
    min-width: calc(var(--jp-cell-prompt-width) * 0.75);
    }

    .jp-ActiveCellTool-CellContent > pre {
    padding: 5px 4px;
    margin: 0;
    white-space: normal;
    }

    .jp-MetadataEditorTool {
    flex-direction: column;
    padding: 12px 0;
    }

    .jp-RankedPanel > :not(:first-child) {
    margin-top: 12px;
    }

    .jp-KeySelector select.jp-mod-styled {
    font-size: var(--jp-ui-font-size1);
    color: var(--jp-ui-font-color0);
    border: var(--jp-border-width) solid var(--jp-border-color1);
    }

    .jp-KeySelector label,
    .jp-MetadataEditorTool label,
    .jp-NumberSetter label {
    line-height: 1.4;
    }

    .jp-NotebookTools .jp-select-wrapper {
    margin-top: 4px;
    margin-bottom: 0;
    }

    .jp-NumberSetter input {
    width: 100%;
    margin-top: 4px;
    }

    .jp-NotebookTools .jp-Collapse {
    margin-top: 16px;
    }

    /*-----------------------------------------------------------------------------
    | Presentation Mode (.jp-mod-presentationMode)
    |----------------------------------------------------------------------------*/

    .jp-mod-presentationMode .jp-Notebook {
    --jp-content-font-size1: var(--jp-content-presentation-font-size1);
    --jp-code-font-size: var(--jp-code-presentation-font-size);
    }

    .jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
    .jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
    flex: 0 0 110px;
    }

    /*-----------------------------------------------------------------------------
    | Side-by-side Mode (.jp-mod-sideBySide)
    |----------------------------------------------------------------------------*/
    .jp-mod-sideBySide.jp-Notebook .jp-Notebook-cell {
    margin-top: 3em;
    margin-bottom: 3em;
    margin-left: 5%;
    margin-right: 5%;
    }

    .jp-mod-sideBySide.jp-Notebook .jp-CodeCell {
    display: grid;
    grid-template-columns: minmax(0, 1fr) min-content minmax(
        0,
        var(--jp-side-by-side-output-size)
        );
    grid-template-rows: auto minmax(0, 1fr) auto;
    grid-template-areas:
        'header header header'
        'input handle output'
        'footer footer footer';
    }

    .jp-mod-sideBySide.jp-Notebook .jp-CodeCell.jp-mod-resizedCell {
    grid-template-columns: minmax(0, 1fr) min-content minmax(
        0,
        var(--jp-side-by-side-resized-cell)
        );
    }

    .jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellHeader {
    grid-area: header;
    }

    .jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-inputWrapper {
    grid-area: input;
    }

    .jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-outputWrapper {
    /* overwrite the default margin (no vertical separation needed in side by side move */
    margin-top: 0;
    grid-area: output;
    }

    .jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellFooter {
    grid-area: footer;
    }

    .jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle {
    grid-area: handle;
    user-select: none;
    display: block;
    height: 100%;
    cursor: ew-resize;
    padding: 0 var(--jp-cell-padding);
    }

    .jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle::after {
    content: '';
    display: block;
    background: var(--jp-border-color2);
    height: 100%;
    width: 5px;
    }

    .jp-mod-sideBySide.jp-Notebook
    .jp-CodeCell.jp-mod-resizedCell
    .jp-CellResizeHandle::after {
    background: var(--jp-border-color0);
    }

    .jp-CellResizeHandle {
    display: none;
    }

    /*-----------------------------------------------------------------------------
    | Placeholder
    |----------------------------------------------------------------------------*/

    .jp-Cell-Placeholder {
    padding-left: 55px;
    }

    .jp-Cell-Placeholder-wrapper {
    background: #fff;
    border: 1px solid;
    border-color: #e5e6e9 #dfe0e4 #d0d1d5;
    border-radius: 4px;
    -webkit-border-radius: 4px;
    margin: 10px 15px;
    }

    .jp-Cell-Placeholder-wrapper-inner {
    padding: 15px;
    position: relative;
    }

    .jp-Cell-Placeholder-wrapper-body {
    background-repeat: repeat;
    background-size: 50% auto;
    }

    .jp-Cell-Placeholder-wrapper-body div {
    background: #f6f7f8;
    background-image: -webkit-linear-gradient(
        left,
        #f6f7f8 0%,
        #edeef1 20%,
        #f6f7f8 40%,
        #f6f7f8 100%
    );
    background-repeat: no-repeat;
    background-size: 800px 104px;
    height: 104px;
    position: absolute;
    right: 15px;
    left: 15px;
    top: 15px;
    }

    div.jp-Cell-Placeholder-h1 {
    top: 20px;
    height: 20px;
    left: 15px;
    width: 150px;
    }

    div.jp-Cell-Placeholder-h2 {
    left: 15px;
    top: 50px;
    height: 10px;
    width: 100px;
    }

    div.jp-Cell-Placeholder-content-1,
    div.jp-Cell-Placeholder-content-2,
    div.jp-Cell-Placeholder-content-3 {
    left: 15px;
    right: 15px;
    height: 10px;
    }

    div.jp-Cell-Placeholder-content-1 {
    top: 100px;
    }

    div.jp-Cell-Placeholder-content-2 {
    top: 120px;
    }

    div.jp-Cell-Placeholder-content-3 {
    top: 140px;
    }

    </style>
    <style type="text/css">
    /*-----------------------------------------------------------------------------
    | Copyright (c) Jupyter Development Team.
    | Distributed under the terms of the Modified BSD License.
    |----------------------------------------------------------------------------*/

    /*
    The following CSS variables define the main, public API for styling JupyterLab.
    These variables should be used by all plugins wherever possible. In other
    words, plugins should not define custom colors, sizes, etc unless absolutely
    necessary. This enables users to change the visual theme of JupyterLab
    by changing these variables.

    Many variables appear in an ordered sequence (0,1,2,3). These sequences
    are designed to work well together, so for example, `--jp-border-color1` should
    be used with `--jp-layout-color1`. The numbers have the following meanings:

    * 0: super-primary, reserved for special emphasis
    * 1: primary, most important under normal situations
    * 2: secondary, next most important under normal situations
    * 3: tertiary, next most important under normal situations

    Throughout JupyterLab, we are mostly following principles from Google's
    Material Design when selecting colors. We are not, however, following
    all of MD as it is not optimized for dense, information rich UIs.
    */

    :root {
    /* Elevation
    *
    * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
    *
    * https://github.com/material-components/material-components-web
    * https://material-components-web.appspot.com/elevation.html
    */

    --jp-shadow-base-lightness: 0;
    --jp-shadow-umbra-color: rgba(
        var(--jp-shadow-base-lightness),
        var(--jp-shadow-base-lightness),
        var(--jp-shadow-base-lightness),
        0.2
    );
    --jp-shadow-penumbra-color: rgba(
        var(--jp-shadow-base-lightness),
        var(--jp-shadow-base-lightness),
        var(--jp-shadow-base-lightness),
        0.14
    );
    --jp-shadow-ambient-color: rgba(
        var(--jp-shadow-base-lightness),
        var(--jp-shadow-base-lightness),
        var(--jp-shadow-base-lightness),
        0.12
    );
    --jp-elevation-z0: none;
    --jp-elevation-z1: 0 2px 1px -1px var(--jp-shadow-umbra-color),
        0 1px 1px 0 var(--jp-shadow-penumbra-color),
        0 1px 3px 0 var(--jp-shadow-ambient-color);
    --jp-elevation-z2: 0 3px 1px -2px var(--jp-shadow-umbra-color),
        0 2px 2px 0 var(--jp-shadow-penumbra-color),
        0 1px 5px 0 var(--jp-shadow-ambient-color);
    --jp-elevation-z4: 0 2px 4px -1px var(--jp-shadow-umbra-color),
        0 4px 5px 0 var(--jp-shadow-penumbra-color),
        0 1px 10px 0 var(--jp-shadow-ambient-color);
    --jp-elevation-z6: 0 3px 5px -1px var(--jp-shadow-umbra-color),
        0 6px 10px 0 var(--jp-shadow-penumbra-color),
        0 1px 18px 0 var(--jp-shadow-ambient-color);
    --jp-elevation-z8: 0 5px 5px -3px var(--jp-shadow-umbra-color),
        0 8px 10px 1px var(--jp-shadow-penumbra-color),
        0 3px 14px 2px var(--jp-shadow-ambient-color);
    --jp-elevation-z12: 0 7px 8px -4px var(--jp-shadow-umbra-color),
        0 12px 17px 2px var(--jp-shadow-penumbra-color),
        0 5px 22px 4px var(--jp-shadow-ambient-color);
    --jp-elevation-z16: 0 8px 10px -5px var(--jp-shadow-umbra-color),
        0 16px 24px 2px var(--jp-shadow-penumbra-color),
        0 6px 30px 5px var(--jp-shadow-ambient-color);
    --jp-elevation-z20: 0 10px 13px -6px var(--jp-shadow-umbra-color),
        0 20px 31px 3px var(--jp-shadow-penumbra-color),
        0 8px 38px 7px var(--jp-shadow-ambient-color);
    --jp-elevation-z24: 0 11px 15px -7px var(--jp-shadow-umbra-color),
        0 24px 38px 3px var(--jp-shadow-penumbra-color),
        0 9px 46px 8px var(--jp-shadow-ambient-color);

    /* Borders
    *
    * The following variables, specify the visual styling of borders in JupyterLab.
    */

    --jp-border-width: 1px;
    --jp-border-color0: var(--md-grey-400);
    --jp-border-color1: var(--md-grey-400);
    --jp-border-color2: var(--md-grey-300);
    --jp-border-color3: var(--md-grey-200);
    --jp-inverse-border-color: var(--md-grey-600);
    --jp-border-radius: 2px;

    /* UI Fonts
    *
    * The UI font CSS variables are used for the typography all of the JupyterLab
    * user interface elements that are not directly user generated content.
    *
    * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
    * is applied to a parent element. When children elements, such as headings, are sized
    * in em all things will be computed relative to that body size.
    */

    --jp-ui-font-scale-factor: 1.2;
    --jp-ui-font-size0: 0.83333em;
    --jp-ui-font-size1: 13px; /* Base font size */
    --jp-ui-font-size2: 1.2em;
    --jp-ui-font-size3: 1.44em;
    --jp-ui-font-family: system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI',
        helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
        'Segoe UI Symbol';

    /*
    * Use these font colors against the corresponding main layout colors.
    * In a light theme, these go from dark to light.
    */

    /* Defaults use Material Design specification */
    --jp-ui-font-color0: rgba(0, 0, 0, 1);
    --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
    --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
    --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

    /*
    * Use these against the brand/accent/warn/error colors.
    * These will typically go from light to darker, in both a dark and light theme.
    */

    --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
    --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
    --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
    --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

    /* Content Fonts
    *
    * Content font variables are used for typography of user generated content.
    *
    * The font sizing here is done assuming that the body font size of --jp-content-font-size1
    * is applied to a parent element. When children elements, such as headings, are sized
    * in em all things will be computed relative to that body size.
    */

    --jp-content-line-height: 1.6;
    --jp-content-font-scale-factor: 1.2;
    --jp-content-font-size0: 0.83333em;
    --jp-content-font-size1: 14px; /* Base font size */
    --jp-content-font-size2: 1.2em;
    --jp-content-font-size3: 1.44em;
    --jp-content-font-size4: 1.728em;
    --jp-content-font-size5: 2.0736em;

    /* This gives a magnification of about 125% in presentation mode over normal. */
    --jp-content-presentation-font-size1: 17px;
    --jp-content-heading-line-height: 1;
    --jp-content-heading-margin-top: 1.2em;
    --jp-content-heading-margin-bottom: 0.8em;
    --jp-content-heading-font-weight: 500;

    /* Defaults use Material Design specification */
    --jp-content-font-color0: rgba(0, 0, 0, 1);
    --jp-content-font-color1: rgba(0, 0, 0, 0.87);
    --jp-content-font-color2: rgba(0, 0, 0, 0.54);
    --jp-content-font-color3: rgba(0, 0, 0, 0.38);
    --jp-content-link-color: var(--md-blue-900);
    --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
        'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
        'Segoe UI Emoji', 'Segoe UI Symbol';

    /*
    * Code Fonts
    *
    * Code font variables are used for typography of code and other monospaces content.
    */

    --jp-code-font-size: 13px;
    --jp-code-line-height: 1.3077; /* 17px for 13px base */
    --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
    --jp-code-font-family-default: menlo, consolas, 'DejaVu Sans Mono', monospace;
    --jp-code-font-family: var(--jp-code-font-family-default);

    /* This gives a magnification of about 125% in presentation mode over normal. */
    --jp-code-presentation-font-size: 16px;

    /* may need to tweak cursor width if you change font size */
    --jp-code-cursor-width0: 1.4px;
    --jp-code-cursor-width1: 2px;
    --jp-code-cursor-width2: 4px;

    /* Layout
    *
    * The following are the main layout colors use in JupyterLab. In a light
    * theme these would go from light to dark.
    */

    --jp-layout-color0: white;
    --jp-layout-color1: white;
    --jp-layout-color2: var(--md-grey-200);
    --jp-layout-color3: var(--md-grey-400);
    --jp-layout-color4: var(--md-grey-600);

    /* Inverse Layout
    *
    * The following are the inverse layout colors use in JupyterLab. In a light
    * theme these would go from dark to light.
    */

    --jp-inverse-layout-color0: #111;
    --jp-inverse-layout-color1: var(--md-grey-900);
    --jp-inverse-layout-color2: var(--md-grey-800);
    --jp-inverse-layout-color3: var(--md-grey-700);
    --jp-inverse-layout-color4: var(--md-grey-600);

    /* Brand/accent */

    --jp-brand-color0: var(--md-blue-900);
    --jp-brand-color1: var(--md-blue-700);
    --jp-brand-color2: var(--md-blue-300);
    --jp-brand-color3: var(--md-blue-100);
    --jp-brand-color4: var(--md-blue-50);
    --jp-accent-color0: var(--md-green-900);
    --jp-accent-color1: var(--md-green-700);
    --jp-accent-color2: var(--md-green-300);
    --jp-accent-color3: var(--md-green-100);

    /* State colors (warn, error, success, info) */

    --jp-warn-color0: var(--md-orange-900);
    --jp-warn-color1: var(--md-orange-700);
    --jp-warn-color2: var(--md-orange-300);
    --jp-warn-color3: var(--md-orange-100);
    --jp-error-color0: var(--md-red-900);
    --jp-error-color1: var(--md-red-700);
    --jp-error-color2: var(--md-red-300);
    --jp-error-color3: var(--md-red-100);
    --jp-success-color0: var(--md-green-900);
    --jp-success-color1: var(--md-green-700);
    --jp-success-color2: var(--md-green-300);
    --jp-success-color3: var(--md-green-100);
    --jp-info-color0: var(--md-cyan-900);
    --jp-info-color1: var(--md-cyan-700);
    --jp-info-color2: var(--md-cyan-300);
    --jp-info-color3: var(--md-cyan-100);

    /* Cell specific styles */

    --jp-cell-padding: 5px;
    --jp-cell-collapser-width: 8px;
    --jp-cell-collapser-min-height: 20px;
    --jp-cell-collapser-not-active-hover-opacity: 0.6;
    --jp-cell-editor-background: var(--md-grey-100);
    --jp-cell-editor-border-color: var(--md-grey-300);
    --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
    --jp-cell-editor-active-background: var(--jp-layout-color0);
    --jp-cell-editor-active-border-color: var(--jp-brand-color1);
    --jp-cell-prompt-width: 64px;
    --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
    --jp-cell-prompt-letter-spacing: 0;
    --jp-cell-prompt-opacity: 1;
    --jp-cell-prompt-not-active-opacity: 0.5;
    --jp-cell-prompt-not-active-font-color: var(--md-grey-700);

    /* A custom blend of MD grey and blue 600
    * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
    --jp-cell-inprompt-font-color: #307fc1;

    /* A custom blend of MD grey and orange 600
    * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
    --jp-cell-outprompt-font-color: #bf5b3d;

    /* Notebook specific styles */

    --jp-notebook-padding: 10px;
    --jp-notebook-select-background: var(--jp-layout-color1);
    --jp-notebook-multiselected-color: var(--md-blue-50);

    /* The scroll padding is calculated to fill enough space at the bottom of the
    notebook to show one single-line cell (with appropriate padding) at the top
    when the notebook is scrolled all the way to the bottom. We also subtract one
    pixel so that no scrollbar appears if we have just one single-line cell in the
    notebook. This padding is to enable a 'scroll past end' feature in a notebook.
    */
    --jp-notebook-scroll-padding: calc(
        100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
        var(--jp-code-padding) - var(--jp-cell-padding) - 1px
    );

    /* Rendermime styles */

    --jp-rendermime-error-background: #fdd;
    --jp-rendermime-table-row-background: var(--md-grey-100);
    --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

    /* Dialog specific styles */

    --jp-dialog-background: rgba(0, 0, 0, 0.25);

    /* Console specific styles */

    --jp-console-padding: 10px;

    /* Toolbar specific styles */

    --jp-toolbar-border-color: var(--jp-border-color1);
    --jp-toolbar-micro-height: 8px;
    --jp-toolbar-background: var(--jp-layout-color1);
    --jp-toolbar-box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.24);
    --jp-toolbar-header-margin: 4px 4px 0 4px;
    --jp-toolbar-active-background: var(--md-grey-300);

    /* Statusbar specific styles */

    --jp-statusbar-height: 24px;

    /* Input field styles */

    --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
    --jp-input-active-background: var(--jp-layout-color1);
    --jp-input-hover-background: var(--jp-layout-color1);
    --jp-input-background: var(--md-grey-100);
    --jp-input-border-color: var(--jp-inverse-border-color);
    --jp-input-active-border-color: var(--jp-brand-color1);
    --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

    /* General editor styles */

    --jp-editor-selected-background: #d9d9d9;
    --jp-editor-selected-focused-background: #d7d4f0;
    --jp-editor-cursor-color: var(--jp-ui-font-color0);

    /* Code mirror specific styles */

    --jp-mirror-editor-keyword-color: #008000;
    --jp-mirror-editor-atom-color: #88f;
    --jp-mirror-editor-number-color: #080;
    --jp-mirror-editor-def-color: #00f;
    --jp-mirror-editor-variable-color: var(--md-grey-900);
    --jp-mirror-editor-variable-2-color: rgb(0, 54, 109);
    --jp-mirror-editor-variable-3-color: #085;
    --jp-mirror-editor-punctuation-color: #05a;
    --jp-mirror-editor-property-color: #05a;
    --jp-mirror-editor-operator-color: #a2f;
    --jp-mirror-editor-comment-color: #408080;
    --jp-mirror-editor-string-color: #ba2121;
    --jp-mirror-editor-string-2-color: #708;
    --jp-mirror-editor-meta-color: #a2f;
    --jp-mirror-editor-qualifier-color: #555;
    --jp-mirror-editor-builtin-color: #008000;
    --jp-mirror-editor-bracket-color: #997;
    --jp-mirror-editor-tag-color: #170;
    --jp-mirror-editor-attribute-color: #00c;
    --jp-mirror-editor-header-color: blue;
    --jp-mirror-editor-quote-color: #090;
    --jp-mirror-editor-link-color: #00c;
    --jp-mirror-editor-error-color: #f00;
    --jp-mirror-editor-hr-color: #999;

    /*
        RTC user specific colors.
        These colors are used for the cursor, username in the editor,
        and the icon of the user.
    */

    --jp-collaborator-color1: #ffad8e;
    --jp-collaborator-color2: #dac83d;
    --jp-collaborator-color3: #72dd76;
    --jp-collaborator-color4: #00e4d0;
    --jp-collaborator-color5: #45d4ff;
    --jp-collaborator-color6: #e2b1ff;
    --jp-collaborator-color7: #ff9de6;

    /* Vega extension styles */

    --jp-vega-background: white;

    /* Sidebar-related styles */

    --jp-sidebar-min-width: 250px;

    /* Search-related styles */

    --jp-search-toggle-off-opacity: 0.5;
    --jp-search-toggle-hover-opacity: 0.8;
    --jp-search-toggle-on-opacity: 1;
    --jp-search-selected-match-background-color: rgb(245, 200, 0);
    --jp-search-selected-match-color: black;
    --jp-search-unselected-match-background-color: var(
        --jp-inverse-layout-color0
    );
    --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

    /* Icon colors that work well with light or dark backgrounds */
    --jp-icon-contrast-color0: var(--md-purple-600);
    --jp-icon-contrast-color1: var(--md-green-600);
    --jp-icon-contrast-color2: var(--md-pink-600);
    --jp-icon-contrast-color3: var(--md-blue-600);

    /* Button colors */
    --jp-accept-color-normal: var(--md-blue-700);
    --jp-accept-color-hover: var(--md-blue-800);
    --jp-accept-color-active: var(--md-blue-900);
    --jp-warn-color-normal: var(--md-red-700);
    --jp-warn-color-hover: var(--md-red-800);
    --jp-warn-color-active: var(--md-red-900);
    --jp-reject-color-normal: var(--md-grey-600);
    --jp-reject-color-hover: var(--md-grey-700);
    --jp-reject-color-active: var(--md-grey-800);

    /* File or activity icons and switch semantic variables */
    --jp-jupyter-icon-color: #f37626;
    --jp-notebook-icon-color: #f37626;
    --jp-json-icon-color: var(--md-orange-700);
    --jp-console-icon-background-color: var(--md-blue-700);
    --jp-console-icon-color: white;
    --jp-terminal-icon-background-color: var(--md-grey-800);
    --jp-terminal-icon-color: var(--md-grey-200);
    --jp-text-editor-icon-color: var(--md-grey-700);
    --jp-inspector-icon-color: var(--md-grey-700);
    --jp-switch-color: var(--md-grey-400);
    --jp-switch-true-position-color: var(--md-orange-900);
    }
    </style>
    <style type="text/css">
    /* Force rendering true colors when outputing to pdf */
    * {
    -webkit-print-color-adjust: exact;
    }

    /* Misc */
    a.anchor-link {
    display: none;
    }

    /* Input area styling */
    .jp-InputArea {
    overflow: hidden;
    }

    .jp-InputArea-editor {
    overflow: hidden;
    }

    .cm-editor.cm-s-jupyter .highlight pre {
    /* weird, but --jp-code-padding defined to be 5px but 4px horizontal padding is hardcoded for pre.cm-line */
    padding: var(--jp-code-padding) 4px;
    margin: 0;

    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
    color: inherit;

    }

    .jp-OutputArea-output pre {
    line-height: inherit;
    font-family: inherit;
    }

    .jp-RenderedText pre {
    color: var(--jp-content-font-color1);
    font-size: var(--jp-code-font-size);
    }

    /* Hiding the collapser by default */
    .jp-Collapser {
    display: none;
    }

    @page {
        margin: 0.5in; /* Margin for each printed piece of paper */
    }

    @media print {
    .jp-Cell-inputWrapper,
    .jp-Cell-outputWrapper {
        display: block;
    }
    }
    </style>
    <!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
        init_mathjax = function() {
            if (window.MathJax) {
            // MathJax loaded
                MathJax.Hub.Config({
                    TeX: {
                        equationNumbers: {
                        autoNumber: "AMS",
                        useLabelIds: true
                        }
                    },
                    tex2jax: {
                        inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                        displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                        processEscapes: true,
                        processEnvironments: true
                    },
                    displayAlign: 'center',
                    CommonHTML: {
                        linebreaks: {
                        automatic: true
                        }
                    }
                });

                MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
            }
        }
        init_mathjax();
        </script>
    <!-- End of mathjax configuration --><script type="module">
    document.addEventListener("DOMContentLoaded", async () => {
        const diagrams = document.querySelectorAll(".jp-Mermaid > pre.mermaid");
        // do not load mermaidjs if not needed
        if (!diagrams.length) {
        return;
        }
        const mermaid = (await import("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.7.0/mermaid.esm.min.mjs")).default;
        const parser = new DOMParser();

        mermaid.initialize({
        maxTextSize: 100000,
        startOnLoad: false,
        fontFamily: window
            .getComputedStyle(document.body)
            .getPropertyValue("--jp-ui-font-family"),
        theme: document.querySelector("body[data-jp-theme-light='true']")
            ? "default"
            : "dark",
        });

        let _nextMermaidId = 0;

        function makeMermaidImage(svg) {
        const img = document.createElement("img");
        const doc = parser.parseFromString(svg, "image/svg+xml");
        const svgEl = doc.querySelector("svg");
        const { maxWidth } = svgEl?.style || {};
        const firstTitle = doc.querySelector("title");
        const firstDesc = doc.querySelector("desc");

        img.setAttribute("src", `data:image/svg+xml,${encodeURIComponent(svg)}`);
        if (maxWidth) {
            img.width = parseInt(maxWidth);
        }
        if (firstTitle) {
            img.setAttribute("alt", firstTitle.textContent);
        }
        if (firstDesc) {
            const caption = document.createElement("figcaption");
            caption.className = "sr-only";
            caption.textContent = firstDesc.textContent;
            return [img, caption];
        }
        return [img];
        }

        async function makeMermaidError(text) {
        let errorMessage = "";
        try {
            await mermaid.parse(text);
        } catch (err) {
            errorMessage = `${err}`;
        }

        const result = document.createElement("details");
        result.className = 'jp-RenderedMermaid-Details';
        const summary = document.createElement("summary");
        summary.className = 'jp-RenderedMermaid-Summary';
        const pre = document.createElement("pre");
        const code = document.createElement("code");
        code.innerText = text;
        pre.appendChild(code);
        summary.appendChild(pre);
        result.appendChild(summary);

        const warning = document.createElement("pre");
        warning.innerText = errorMessage;
        result.appendChild(warning);
        return [result];
        }

        async function renderOneMarmaid(src) {
        const id = `jp-mermaid-${_nextMermaidId++}`;
        const parent = src.parentNode;
        let raw = src.textContent.trim();
        const el = document.createElement("div");
        el.style.visibility = "hidden";
        document.body.appendChild(el);
        let results = null;
        let output = null;
        try {
            const { svg } = await mermaid.render(id, raw, el);
            results = makeMermaidImage(svg);
            output = document.createElement("figure");
            results.map(output.appendChild, output);
        } catch (err) {
            parent.classList.add("jp-mod-warning");
            results = await makeMermaidError(raw);
            output = results[0];
        } finally {
            el.remove();
        }
        parent.classList.add("jp-RenderedMermaid");
        parent.appendChild(output);
        }

        void Promise.all([...diagrams].map(renderOneMarmaid));
    });
    </script>
    <style>
    .jp-Mermaid:not(.jp-RenderedMermaid) {
        display: none;
    }

    .jp-RenderedMermaid {
        overflow: auto;
        display: flex;
    }

    .jp-RenderedMermaid.jp-mod-warning {
        width: auto;
        padding: 0.5em;
        margin-top: 0.5em;
        border: var(--jp-border-width) solid var(--jp-warn-color2);
        border-radius: var(--jp-border-radius);
        color: var(--jp-ui-font-color1);
        font-size: var(--jp-ui-font-size1);
        white-space: pre-wrap;
        word-wrap: break-word;
    }

    .jp-RenderedMermaid figure {
        margin: 0;
        overflow: auto;
        max-width: 100%;
    }

    .jp-RenderedMermaid img {
        max-width: 100%;
    }

    .jp-RenderedMermaid-Details > pre {
        margin-top: 1em;
    }

    .jp-RenderedMermaid-Summary {
        color: var(--jp-warn-color2);
    }

    .jp-RenderedMermaid:not(.jp-mod-warning) pre {
        display: none;
    }

    .jp-RenderedMermaid-Summary > pre {
        display: inline-block;
        white-space: normal;
    }
    </style>
    <!-- End of mermaid configuration --></head>
    <body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
    <main><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span> 
    <span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span> 
    <span class="kn">import</span> <span class="nn">joblib</span>

    <span class="c1"># for plotting graphs</span>
    <span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span> 
    <span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr" tabindex="0">
    <pre>C:\Users\DELL\anaconda3\Lib\site-packages\pandas\core\arrays\masked.py:60: UserWarning: Pandas requires version '1.3.6' or newer of 'bottleneck' (version '1.3.5' currently installed).
    from pandas.core import (
    </pre>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [2]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Style settings</span>
    <span class="o">%</span><span class="k">matplotlib</span> inline
    <span class="n">sns</span><span class="o">.</span><span class="n">set_style</span><span class="p">(</span><span class="s2">"darkgrid"</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Import Dataset</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [4]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">"../data/dementia_dataset.csv"</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [5]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[5]:</div>
    <div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
    <div>
    <style scoped="">
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
    <thead>
    <tr style="text-align: right;">
    <th></th>
    <th>Subject ID</th>
    <th>MRI ID</th>
    <th>Group</th>
    <th>Visit</th>
    <th>MR Delay</th>
    <th>M/F</th>
    <th>Hand</th>
    <th>Age</th>
    <th>EDUC</th>
    <th>SES</th>
    <th>MMSE</th>
    <th>CDR</th>
    <th>eTIV</th>
    <th>nWBV</th>
    <th>ASF</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <th>0</th>
    <td>OAS2_0001</td>
    <td>OAS2_0001_MR1</td>
    <td>Nondemented</td>
    <td>1</td>
    <td>0</td>
    <td>M</td>
    <td>R</td>
    <td>87</td>
    <td>14</td>
    <td>2.0</td>
    <td>27.0</td>
    <td>0.0</td>
    <td>1987</td>
    <td>0.696</td>
    <td>0.883</td>
    </tr>
    <tr>
    <th>1</th>
    <td>OAS2_0001</td>
    <td>OAS2_0001_MR2</td>
    <td>Nondemented</td>
    <td>2</td>
    <td>457</td>
    <td>M</td>
    <td>R</td>
    <td>88</td>
    <td>14</td>
    <td>2.0</td>
    <td>30.0</td>
    <td>0.0</td>
    <td>2004</td>
    <td>0.681</td>
    <td>0.876</td>
    </tr>
    <tr>
    <th>2</th>
    <td>OAS2_0002</td>
    <td>OAS2_0002_MR1</td>
    <td>Demented</td>
    <td>1</td>
    <td>0</td>
    <td>M</td>
    <td>R</td>
    <td>75</td>
    <td>12</td>
    <td>NaN</td>
    <td>23.0</td>
    <td>0.5</td>
    <td>1678</td>
    <td>0.736</td>
    <td>1.046</td>
    </tr>
    <tr>
    <th>3</th>
    <td>OAS2_0002</td>
    <td>OAS2_0002_MR2</td>
    <td>Demented</td>
    <td>2</td>
    <td>560</td>
    <td>M</td>
    <td>R</td>
    <td>76</td>
    <td>12</td>
    <td>NaN</td>
    <td>28.0</td>
    <td>0.5</td>
    <td>1738</td>
    <td>0.713</td>
    <td>1.010</td>
    </tr>
    <tr>
    <th>4</th>
    <td>OAS2_0002</td>
    <td>OAS2_0002_MR3</td>
    <td>Demented</td>
    <td>3</td>
    <td>1895</td>
    <td>M</td>
    <td>R</td>
    <td>80</td>
    <td>12</td>
    <td>NaN</td>
    <td>22.0</td>
    <td>0.5</td>
    <td>1698</td>
    <td>0.701</td>
    <td>1.034</td>
    </tr>
    </tbody>
    </table>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Check basic information of the dataset</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [6]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
    <pre>&lt;class 'pandas.core.frame.DataFrame'&gt;
    RangeIndex: 373 entries, 0 to 372
    Data columns (total 15 columns):
    #   Column      Non-Null Count  Dtype  
    ---  ------      --------------  -----  
    0   Subject ID  373 non-null    object 
    1   MRI ID      373 non-null    object 
    2   Group       373 non-null    object 
    3   Visit       373 non-null    int64  
    4   MR Delay    373 non-null    int64  
    5   M/F         373 non-null    object 
    6   Hand        373 non-null    object 
    7   Age         373 non-null    int64  
    8   EDUC        373 non-null    int64  
    9   SES         354 non-null    float64
    10  MMSE        371 non-null    float64
    11  CDR         373 non-null    float64
    12  eTIV        373 non-null    int64  
    13  nWBV        373 non-null    float64
    14  ASF         373 non-null    float64
    dtypes: float64(5), int64(5), object(5)
    memory usage: 43.8+ KB
    </pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h2 id="Data-Preprocessing">Data Preprocessing<a class="anchor-link" href="#Data-Preprocessing">¶</a></h2>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h3 id="Feature-Engineering">Feature Engineering<a class="anchor-link" href="#Feature-Engineering">¶</a></h3>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Mapping Ordinal values to numerical values</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [7]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">group</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"Nondemented"</span> <span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
        <span class="s2">"Demented"</span> <span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="s2">"Converted"</span> <span class="p">:</span> <span class="mi">2</span>
    <span class="p">}</span>
    <span class="n">dementia</span><span class="p">[</span><span class="s2">"Group"</span><span class="p">]</span> <span class="o">=</span> <span class="n">dementia</span><span class="p">[</span><span class="s2">"Group"</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">group</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [8]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">gender</span> <span class="o">=</span> <span class="p">{</span>
        <span class="s2">"M"</span> <span class="p">:</span> <span class="mi">1</span><span class="p">,</span>
        <span class="s2">"F"</span> <span class="p">:</span> <span class="mi">0</span>
    <span class="p">}</span>
    <span class="n">dementia</span><span class="p">[</span><span class="s2">"M/F"</span><span class="p">]</span> <span class="o">=</span> <span class="n">dementia</span><span class="p">[</span><span class="s2">"M/F"</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">gender</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Correlations</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [119]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">[</span><span class="mi">10</span><span class="p">,</span> <span class="mi">8</span><span class="p">])</span>
    <span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">dementia</span><span class="o">.</span><span class="n">corr</span><span class="p">(),</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cbar</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">cmap</span><span class="o">=</span><span class="s2">"Reds"</span><span class="p">);</span>
    <span class="c1"># (MR delay-Visit*), (educ-ses), (etiv-asf*) high correlated</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
    <img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAkwAAAHRCAYAAACYdObDAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAD39klEQVR4nOzdd5gTVd/G8e+ZSbLJFnpvy1KX3gUUVEBA4cGCShUUCyKIoIKAioiNJkVAsTdEAbFTLDRpgvTee+9tSzbJzHn/mCXZALuL+2yy6/Oez3V5SXLOZO/MTs785sxMVkgpJYqiKIqiKEq6tJwOoCiKoiiKktupgklRFEVRFCUTqmBSFEVRFEXJhCqYFEVRFEVRMqEKJkVRFEVRlEyogklRFEVRFCUTtlC+eC+RJ5QvH1KTn2uZ0xGyRoicTpBlKXuP53SELLEXiMrpCFmmFS+S0xGyxu3O6QRZJmrVzekIWbJ8wHs5HSHLbn745pyOkCUiNjanI2SZsX5TTkfIEsfHv6XbpmaYFEVRFEVRMqEKJkVRFEVRlEyogklRFEVRFCUTqmBSFEVRFEXJhCqYFEVRFEVRMnHDd8nNnz+fffv2UbFiRZo1axbKTIqiKIqiKLnKDc0wvfTSS8yePZuIiAh+/PFH3nrrrVDnUhRFURRFyTVuaIZp165dfPvttwA8/PDDdOjQIaShFEVRFEVRcpMbmmEqU6YMhw8fBuDs2bMUL148pKEURVEURVFykxuaYdqwYQN33XUXJUqU4OTJkzgcDpo0aQLAsmXLQhpQURRFURQlp91QwbRgwYJQ51AURVEURcm1bqhgGjJkyDXPjRgxItvDKIqiKIqi5EY3VDC1adMGACkl27Zt49SpUyENpSiKoiiKkpvcUMHUtGlT/79vvfVWHn300ZAFulFlb6pP+1HDGdesbU5HAUBUrY/W8kEwDcy/FyJXzQ/uEBWD1rU/wu5AXjqPOX0yeD3+Zu2BXpCcgDnnK9B0tM59EQUKg2lifPs+nDoaotz1rNyGgbl60bW5I9PmPoc5492rcj8JSQmYc6eBbkPr2AdRsCjSnYz5w0dw5kRIcge/CYHjyQFoZSuA10PKuyORJ65aX44InK9OIOXdEcijhwLP582H6+1Pcb/aP/j5EGbVH+qLKF0OvF58X4yHU8cCzbUaobfram1Hy37DXDIvsGxMPuyvvIt37GA4cRhRpgJ6t2fA50Ue3ovxzRSQMvTv4TpE5Tpoze6zcq/7E7lm8fX7NW6NiMmH+fuM8ObL4nYubv0P2k0tIPESAMasD+B06u8rOg96/9EYH7wWeC7EFu06zJSlG9E1jfa1KvBg3UpB7acTknnhxyV4DZPC0S7eursJLntgmB82ZwV5XRE817xeWPICIAQVRr1FdLWqmCkedj03EPeBA/7mkk8+QbEunfCePQfA7oGDyFO/HkU7Wndja84IoqtV5a8adTEuXQpP5Cr10O64H0zT2l7+vuqylMgYtC7PBMbzme9Z20vTtmgNmge2l+8/RJSphFb/dms5mx1KlMV4vSe4k0L6HhbtO8GUv3eha4L2VcvwYPXYoPZjl5N4ef4GDFMiJQxvUYu4/NFsPnmeUUu3goRCkRGMal2XCJse0qwIgd61L6J0HPi8+L6YcNW42BD9P1fGxd8xl6YdF/NiH/ou3nFD4MRhKF4GW/d+IATy8D6Mr98DaWZLzBsqmNJe2H369GnOnDmTLT88q1oN7EfDbp1ISQztBnfDNB3tnkcwJgwCTwr6029ibFsDly8EurR8ELl+GebqRYjm9yEat0IumQ2AaNQSUbwMct8263GVuqDpGJNeQlSqiXZXF8wvxoQm992PYLwzODX3G+nkXoq5ZjGi2b2IRq2QS9PkLpYmd6M7wOPGmPQiFC6Bdt/jmB+9kf25r6I3vBXsDtyDn0SrVA1Hj76kjBgceA/l43H0GogoWPiqBXUier0AnpSQZ7xC1LkZ7A58b/VHlIvH1qEnvsmv+vPYOj6J942+kOLGNmQ85oaVcOm81da9X1BW/eH+GF+/h9y7Df2+R9AaNsdcmQPXG2o6WpuHMKYMBW8K+hPDMHash4SLgT42O9q9jyNKlUduWx3+fFnczkXJchjfTIKj+659zfufDDp4CDWvYTLyj9XMfLQtLoeNhz6fx+2VSlM42uXv8/GKzdxbswL31CzP5D83MHPdTh5uWA2AGWt3suvUBRrEFg1bZoCCd92JFhHBhrb3EFOvLuWGD2Xbw4/526Nr1mBn3/4kbNrsfy557z5OzrC+yqbCiDc48c2MsBVLaDpau4cxJg0Bjxu99+vW9pJme9bueMAaz9f+ibj9HkSjlsilc6ztZcZkOLrf31eePo6x9k9ruXsfQ65ZFPJiyWuYjFy6hZkdb8Vlt/HQt8u4Pa4ohaOc/j6T/tpBl5px3FG+OMsOnmL8im2806YBryzYyIQ29YnNF82sLQc5djmZuPzRIc1rjYt2fCOetcbFB3vie/dVq1HXsXXsFRgXB4/D3JhmXOwWPC7a2vfA+P4z5O4t6D2eR9RuhFy/Ilty3tDXCsyZM8f/34YNG3L8iytP793PB+0fytEMQYqWQp45AcmJYPiQ+7cj4qoEdRFxVZA71gMgt69DVKxpNcRWQsRWwlz5h7+vPH0MNA2EgIhIMHxhyr3jOrnjkTs3WLl2rEdUqpEmd8Wg3KJoKf975PQxRJGSocl9Fb1KTYz1KwEwd21FKx8f3MFuJ2XkEOTRg0FPOx55Gt9vPyLPhe8AQKtYHbllDQBy3w5E2cAMgSheBnnqGCQlWL+P3VsRlaoDoHfoibF4NvLC2UD//IWQe61i1dy9FVGxWtjeR5DCJZBnT1o7AcNAHtyJiK0c3MdmR25YivnnT+HP919s56JUObQW96H3eR3R/D5/f61dd+Rfv1uDdpjsO3OB2Pwx5HVF4NB16pYuwtpDJ4P6DG7ZgHY1ymFKyYlLiRSMsoqpDUdOsfHoaTpcNSMVDnkbNuD8osUAXF67jphatYLaY2rWoPQzT1Pr5+8p/UyfoLboWjWJrFyZE1OnhSsuFCmJPHtlezGQB3ZeZ3upHNhedm5AVEjdXkrGoTW7D/2p1xDN7g1+3VLlrDFyVegPavadv0xs3ijyOh04dI26JQqw9ti5oD4vNK3GbWWt4tkwJRG6zoELieRzOpi6YR/dZy3nYoon5MUSgFah2lXjYkV/2zXj4p6tiIqp4+KDT2D8OQd5MTAu+t57Hbl7C+g2RN4CcOlC9uW8kU4jRoygR48eNG3alE6dOlG9evVsC5AV67//GcPrzdEMQZyu4COGFDe4Iq/tk5zkbxeuSIjJh9a6I+b3HwX39bgRBYqgD5qI1qEX5rK5ockdcXXuZHBmlDsZ4UzN3aoD5vcfB3WVRw8gqqRO9ZepCHkLgAjDnyt0RUFSYuCxaYAWmEI2d2xGng2+7s7WrA3y4gWMDX+HPl9azkhkUFbTKo6vtCWnaXMnIVxRaLe0RF6+iNy6Nuil5Onj/h27VrsRRDjJEU4XpKTZjjzua7cjdxJyz5bw5roiq9s5YG5YjjnrQ4z3hyPi4hFV6iHq345MuITctTFMb8CSkOIl2unwP45y2ElICZ7hEkJgmJK7P/iJvw+eoE6pIpy+nMS7SzYy9K5GYc17hR4Tg+/SZf9jaRigBz6fp378md0vDGbT/R3Jc9NNFGjZwt9Wpl9fDo4dH9a8147nydeO5xGRgT5pt5eNKzC//wjjw+GIsvHW2YJUWrP7MOfPCnV6ABI8PqIj7P7HUQ4bCSnB+8z8rgjsusb+8wmMWbaV3g0rcz45hQ3Hz9GpRhyf3NeYlYfP8Nfh06EP7Lpq7MtwXExGREah3Xz9cRFpQoEi2F/7EKLzIE8czraYN3RKburUqcyePZuaNWvy6aefctddd/HYY49lvuD/OO3Ozoi4eCgRizy4O9AQ4bSOTtJyJ4PTCQkeiHAikxMRtW5GRMagP/4S5MkPdgfi1FFE8Vjkzg3WdUH5CqL3Go7x9rPgy54iUbuzk3XEVLwM8tCeNLld4M4otwuZnGTljkrNHZPPn1uuXogoWgr9qeHI/TvgyL5sO3ecoeTE4B2g0KyiKQO2Fm0BiV6rPlpcRSL6DSXlrUHIC+cyXO6/5k5COF34rzQSwhoc/G1p3kdqcaXfcS9IiValDqJMeWyPDcQ3aRi+T8di6/wU3NUBuX8XhPkgQrvjAWsmqWhp5JG9gQaH89rtKAf8t9s5gFw6x79jlNvXQck4tEo1rWvFKtWEEmXRO/fF+GxU0Cm+7PTOonWsO3yKnafOU7Nk4LRyosdLTJoC6gq7rjG7172s2HeMIT8vo2V8LOeT3PT6Zj5nEpNJ9hrEFczLfbUqhCTv1YzLl9Gjo/yPhaaBEfh8Hv3wY4zLVkF1bv4CoqtX59wfC9Dz5MFVoTwXl2fP6ZTMaK07IsrGQ/FY5KG047nr2vE8Jcl63ue1tpfU7Ukum2NtS4DcsQ5KxMH2deCMRBQpibl3a0jfwzt/bWfdsXPsPHOJmsXy+59P9PiISVNAXbHq8BleX7yJka3qEpc/GiklZfJFUaFgDABNYouw7dQFGpcufM2y2SrZGvvSHxcDp51xupBJCegt7rXGxap1EKUD4yKXzsO5U3hfehSt6Z3oHZ/E+PTtbIl5QwXT7NmzmTZtGjabDa/XS6dOnVTBBJi/fmP9Q9PRX3gHXNHW7FC5qpiLfw7qKw/sQFSph1y9CFGlLnLfduSyuRips0eiQTNEkZLI1YvgjgcCO/ykBOtoTMu+mRrz1+mB3AMnpMld5fq54+si1yxGxNdB7r8qd/3brdxrFkNsJeT+7Zg/fw6lyqMVLJZtmTNibN+M3uAWjBUL0SpVwzy0N9Nl3C8Hpv6dr08i5f0xoS+WAHPPVrRajWDNEkS5eOTRA/42efwQomhJiIqxjqIq1UD+9i2+tUv9fWwDx+CbOhEunUdr1Bzf52Phwjn0Lr0xN4f32iD/0bKmoz8zyprp87gRZeNDNyv6D/y32znOSPQB4zBG97eWq1Ad+fdCjDSzBPpTw60LwUNULAH0a2bNUngNk3bv/8iF5BQiHTbWHDpJj0bBp2Ffm7eS1lViaVi2OFERdjQh6HZTFbrdZJ1S+mHjHvafvRi2Ygng0t9rKNDqDs78PJuYenVJ3L7D36bHxFD/zwWsbnI7ZlIS+ZrcwolvrBsC8jZuyIWl4ftiZPO31BsRNB19wLjA9hxXBfPPq7eXndZ2svZPROXa1gGi04X+3Fjr4NaTgihf3bpeCRDlqiB3b776R2a7fo2t37PXMGn31SIuuD1E2m2sOXqWHnXLB/VddfgMI5Zs5oN7GlEyj3WgVipvFEleg4MXEojNF83aY2e5v2rsNT8nu5l7tqHVapj+uFjk6nFxFr61gW3DNnA0vqmT4NJ5bE+/im/mh9ZF4+7kbL0R5oYKJiklNpvV1W63Y7dfW6n+v2YamD9/jt5zKAiBuXohXDoHrmi0Dk9hfjEG849ZaJ37ojW8A5l4CXPahHRfTi6ZjdaxD1qf10G3WTNNobgw2TQwf/kcvefLVu6/F12be/53aJ2eTs19GfPr9HNz+jiidSe02+5GupOsO0fCwFj1J3rtBjhHvA9CkDLpTfSmLRFOF74/fs78BcJIrlsOVetiGzIehMD36Vi0hs0gwoW5ZC6+GR9ge/YtEBrmsl8hzTVL17zWyaPY+r0JHjdyx0ZkmAsmP9PAnDcN/eFB1na07k+4fB5cUWj3Po75zTs5kyttvqxs554UzLlfoz/1qnUn4u7NgWv0coBd1xjUsgE9v/4DU0ra165I0TxRXEhO4ZXZK5j4YDMealCF4XP/YsrSTQgBQ+9qmGN5rzgzdx75bmtKrdk/IoRgZ7/nKNz+XvSoKE5Mncb+t0ZR6/uZmB4PF5Yu5/yChQBEli+P++DBTF49BEwD85cvrRl0oWGuXmTNWrii0B7ohTl1LOaC760xumGL1O1lInhTMH/9Bv3JYeDzIfek2V4Kl0CeO5nxz81Gdl1jUNNq9PxxpbWtVC1D0WgXF9weXlmwgYltb2Lk0i14TcmLf1gZy+aPZnjzWrzeohYv/LYOKaF28fzcFhf6mwTk+tRxcfB4EOD7bBzaTc3A6cRcMg/fzA+w9X8TNA1z2W8ZjovGvJnYHh0APh943NYdd9lESJl5+TVq1CiOHj1KvXr1WLt2LSVLlmTQoEGZvngvkSdbQuaEyc+1zOkIWSNETifIspS9x3M6QpbYC0Rl3imX0ooXyekIWeN253SCLBO16mbeKRdaPiA8B0ChcPPDN+d0hCwRsaGf3QkVY/2mnI6QJY6Pf0u37YZmmHr37s3atWvZu3cv7du35/bbb8+ubIqiKIqiKLneDRVMPXv25JtvvlGFkqIoiqIo/y/dUMGUN29evvjiC+Li4tBSLz5u0qRJSIMpiqIoiqLkFjdUMOXPn58///yTHTt2cOzYMUqUKKEKJkVRFEVR/t/I8F71PXv20L17d0aMGMGxY8fYt28fBw4c4K677gpXPkVRFEVRlByXYcH09ttvM3DgQAAKFy7MjBkz+PLLL/noo48yWkxRFEVRFOV/SoYFU3JyMjVqWH96ISbG+ubP2NhYfL4Q/W0zRVEURVGUXCjDgiklJfBlie+9F/gOjitfYqkoiqIoivL/QYYFU5EiRdi0KfjLpzZt2kThwiH+uzKKoiiKoii5SIZTRQMHDqR37940atSI2NhYDh8+zF9//cX7778frnyKoiiKoig5LsMZptKlS/Ptt99Sp04dkpKSqF69OtOnT6dEiRLhyqcoiqIoipLjMr0Yyel00qZNm3BkURRFURRFyZUynGFSFEVRFEVRVMGkKIqiKIqSKSGllKF6cd/z94fqpUPu6XF/5HSELClo13M6Qpa90qluTkfIEu+ZyzkdIcsiShfM6QhZImKicjpC1hlGTifIGq83pxNkmffUxZyOkCWOahVyOkLWha60CCn91c/TbVMzTIqiKIqiKJlQBZOiKIqiKEomVMGkKIqiKIqSCVUwKYqiKIqiZEIVTIqiKIqiKJlQBZOiKIqiKEomVMGkKIqiKIqSCVUwKYqiKIqiZEIVTIqiKIqiKJlQBZOiKIqiKEomMi2YXnvttaDHL7zwQsjCKIqiKIqi5Ea29BqmTZvGlClTuHDhAr///jsAUkoqVPgX/20bRVEURVGULEi3YOratStdu3bl/fffp1evXuHMpCiKoiiKkqukWzAtWrSIZs2akS9fPmbMmBHU1rFjx5CEEVXro7V8EEwD8++FyFXzgztExaB17Y+wO5CXzmNOnwxej79Ze6AXJCdgzvkKNB2tc19EgcJgmhjfvg+njoYk9z9R9qb6tB81nHHN2uZ0lCBCCO6eNJZiNavhS/HwQ69nOLd3v7+9dteONH2uL+6Ll1j35des/fwrNJuN9h9NJn9sGWwRDhaNGMuO2fNyIjy2h/shypQHrwfvJ2Ph1DF/s1a7Mfq9D1nbwZJ5mIvnojVpjd60ldXB7kCUqYDnmQcgKTGsuSP6DEKLqwheD+533kQePxLcJyIC15uTcU94A3nkIOg6Ec+/ilakOJgm7olvWs+HKa/WuQ+idDnwejGmToDTxwPNNRuite1ifX6X/45c9itoOvrDz0LBomCzY879BrlpFZQuj63Pq8jU35O5ZA5yzZLQRa9azxpbDANz9aJrx5bItGPLOcwZ74LXg7j1P2g3tYDESwAYsz6AsyfROvZG5C8CNhvm/O+Q29aELnu1+mitOoBpYq5agFz5R3CHqBi0bs9Z2S+ew/xmkpW9ThO029qBaSKPH8Sc9UFgXCxYFJmSjDnrQzhz/Po/+B8HFdZ6KRkHPi/GtIlBry2q34R2Vyfrffz1B3LFb+kvUzIO/cFeIE2kz4v55Ti4fAFxa1u0hi1AgvnrN8gtq7Mnewbvyf74c2ixFZBeL973RyFPXrUfcUTgeHk83vdHIo8dAl3H/tQQROFiCLsd73dfYq5dHtqc11OpFtqt94BpIDcsRa67/udLNGwJ0XmRC2ZZT1Sph3ZLW0Ai1/6JXB+6z2W6KtVGu+1ua9tdvxS57s/rdhONWlnZ539rPa7e0HpOmsiTR5BzvgQpsy1WugXThQsXADhz5ky2/bAMaTraPY9gTBgEnhT0p9/E2LYGLl8IdGn5IHL9MszVixDN70M0boVcMhsA0aglongZ5L5t1uMqdUHTMSa9hKhUE+2uLphfjAnPe0lHq4H9aNitEymJSTma43qq3NMWmzOCD25tTemb6tNm9Bt8dX9XACILFuCOV1/i3ZtuxX3hIj1+/ZG9i/6k3G1NSTp7jlk9euEqkJ+n/16SIwWTVu8WsDvwvtYXUb4Kti698E14xWrUdWxdn8IzrDekuLEPfQdz/V+Yy37DXPYbALbuz2As+TW8xRKgN74N7A6Sn38MrXJ1Ih7vh/v1gYH3VbEKEU8PRhQsElimwS2g6yQPeBy9zk1EPPwU7jcHhyWvqN0YYXdgjHoOEReP/sATGFNSr3HUdPQHe+Ib0Q9S3OgvjMXYtApRvT4y8TLmZ29DVAy2lyfj27QKUaYC5vwfMOd/H/rgmo529yMY7wxOHVveSGdsWYq5ZjGi2b2IRq2QS2cjSpbD+GYSHN0XWA8NmkHiZev5yGj0Z8dYrxeq7Pc8ijF+oJX9mbcwtq4Ozt6qA3LtEmtcbNEecXNr5Irf0Np0xRjdD7weq6CqWh/yFwKP21oXhUug3f8E5gevpf/z/wFRsxHY7BhjB0DZymjtH8P88I3A+7j/cYzRz1rv47nRGJtXIcpVue4y+gM9rYPco/sRt9yJ1vIBzN9mojVtgzHiGbA70F9+D2NLj2zJnh6tQVOwR5Dy8lOIilWxd++DZ8yLgfdcrjKOJwYgChb2P6c3bQ2XL+KZ/AZE5yFi9KekhLtg0nS01p0xP3oNPCloj76E3LnBX/gDYLMj2vVAlCyH3J66/QqB1uJBzI+Gg8eN1vtN5I51kJwQ3ux3dsb8cDh4U7Pv2gAJF4Oz330l+9rAc83vx5zysnXAcH8vqFQLdm7IvmjpNdx3330A9OnTh4cffphHHnmEUqVK0a1bt2z74UGKlkKeOQHJiWD4kPu3I+KqBHURcVWQO9YDILevQ1SsaTXEVkLEVsJMc+QlTx8DTQMhICISDF9ocv8Dp/fu54P2D+V0jOuKvbkRu35fAMDhv9dQsm5tf1uBuLKc2LSZ5PMXkFJydO16SjdswJbvfmL+q2/5+5m+nFnHolINzE3Wkabcux2tbOVAW4lY64gwKQEMH+auLWiVagTa4yohSsZiLp4T9tx6tdoYa/8CwNy5Ba1i8PaO3Y779YHIIwf8T5lHDyE03dquI6OQYVznokI1zK3W4CT370DEVgw0Fi9tfeZS17PcsxVRoRpy7VLMn74M9DMM67ViKyJqNEAfMBq9W3+IcIUu+DVjy47rjC3x1g4FkDvWI1K3EVGqHFqL+9D7vI5obo2JcuNfmL9NDyxsmiHOfjx4XCxXNTh7uavGxUo1rdmadwYHZuA1HXweRNHSyO3rrOdOH0MULZVtUUX5aoHXPrATUSbN9lGsNPJ0mvexdxuiQrV0lzE+Gw1HU2e4dd16H4mXMEb0BdOAPPmt1woxPb4m5oZVAMjd29DKxwe1C7sDz9svYR495H/O+GsR3hkfBzqlbvNhVag4nDsF7iRrhunwLoitFNzHZkduXI5c+kvgOSkx330RUpLBFW2NMx53eLMXTpPdMJCHdkOZ9LLPDjxn+DA/ecO/zQtNB583W6NlepfcoEGDWLhwIW+//Tbr1q3jxRdfzGyRrHG6rBV0RYobXJHX9klO8rcLVyTE5ENr3RHz+4+C+3rciAJF0AdNROvQC3PZ3NDk/gfWf/8zhjd7f4HZxZknhpSLgaMP0zDRdB2AM3v2UqRKPFFFCmN3uSjf7FYckZF4EhPxJCTgiI6my/Qv+OPVN3Mku3BGBg+e0rCKZQBXJDJtmzsZIqP9D/V2XfD9ODVMSYOJyChkUpojN9O0dmxXHm7bhDxzKnih5CRE0eJEfvgtzmdexPtz8OnyULp2PZv+9SycUcFt7mRwRVmf45RkiHChP/kSRmrxJA/sxPjuE4y3X0CeOYH2n66hCx5x9diSDM6MxpZk670C5oblmLM+xHh/OCIuHlGlnrUDSXFDhBOt+wDMX78JXXZnZHB2t/va7BFp+qQkW78LKf1H5KJpG4hwInduRB7bb800gbUDzVsARDZ9u4zTFbwNmGk+h1dvOynJ4IxKf5lL563HcfFot/4Hc9GPqe0m4tb/oA94G3N9GGZtXMGfUXn1Z3TnZuTZqz6jKcnW9u904XjudXzTr9o3hUOEC+lOTpPJjYi4artxJ8G+rdcuK02Ir4fW6zXkwV3W7yScIlzItNu8x41wXnVA5U6CvVdll9I/gyZuugMcEdf2+S+le0ruiqNHj3LPPfcwa9Yspk6dysMPP5ytAbQ7OyPi4qFELPLg7kBDhPPaIwh3MjidkOCxBoDkREStmxGRMeiPv2QdddgdiFNHEcVjkTs3YM6dBvkKovcajvH2s9lecf6vcF+6jCMmUEgITWCmHhm5L1xk7sCX6DLjSy4dPcax9RtJOnsWgLylStL126msev8TNk2flSPZpTvJGnivEFrgqD85KXgH43RZsyAAkVHWadztG8KWNS2ZlIhwRQWe0ESmg5P9vi4Y61bi+fw9RKEiuEa8R1LvLkHX8oVKRutZuhOtHfcVaXeE+QuhPzUUc/Ec5OrFVv/1K/zt5oYV6J2eyva82p2drJmk4mWQh/YEGiJc4M5obHEhU4snuXSOvxiR29dByTjYvhbyFkR/5AXMFb8h1y/L/ux3dbFOVxWPtY6wr3A6r82ekmS9J++V7KntQqC16w6FS2B+Nsp6D6sWIIqWQu/zOnL/Dji8z9pBZgd3cvBMYdrPofuqz2FE6vaRwTKiblO01h0wprwKCYGDOblkNsbyX9F6D4eKNZC7N2dP/utJTrQOzK/EE5l/RgFEwSI4BryJ7/cfMJbPz7R/dhHN2luzdEVLwZF9+K/eiXAGFyGZ2bEWc8c6xL2PIWrdgtyQ/dv41UTz9ogyla7N7vgH2YVAtOyAKFgMc+bkbM+Y6aGF1+tl7ty5VKhQgXPnzvmvbcou5q/fYEwZhjHsMUSh4tY0oG5DlKuKPLArqK88sMM6wsO6Rknu245cNhdjwgsYU4ZhLvwBuX4ZcvUiZFJCYCUnJVjTulo2HUn9Dzr01yoq39kSgNI31efklu3+Nk3XKd2wPh83b8OsHr0oVLkSB1esIqpIYR6Z+x2/vvgqa7+YllPRkbu2oNVqCIAoXwV5OHCxujx2EFG0JETFgG5Dq1wTc491nZtWuab/FFNOMLZtRK9/c2qW6pgH9ma6jEy4hEy0Cj55+RLYbGHbruWebWjVGwCpp7COBtYzxw8jipSwZu90G1rF6sh92yEmH7Z+b2J+/xlyxe/+7nq/NxBlrWl2Lb528MFSNjF/nW6NLa8+jihYLM3YUuX6Y0t8Xeu9xddB7t8Ozkj0AePA4bSer1AdjuyF6LzoPYdizvkKuXphtucGMOd9jfHuUIxXeiAKFfOvV1GuGvLAzuDs+3dY12xyZVxM3b4ffApsDsxPRwYK6tIVkfu2Y7w7FHPzSuTZE9mWWe7bhqiWOntVtjLy2IFA44nDiMKB7UNUqI7cvyPdZUSD29Fu/Q/GO0Pg7EmrvUhJtMdTz3AYPvB5kdl4Qe/1GDs3o9VpbGWqWBXz0L5MlgDy5sfx0li8097HWBTeMxty0feYX4zCfLs/FChqzeJpOqJMZTiyJ9PlcTjRHh4Eug2Q4E3J1oumMyIXfo/5+UjMMf2gQBFrhlrXEbGV4fANZAfEfx6xbi6ZPjEkB5FCZrLF/f7778yZM4chQ4YwY8YMatasSbNmzW7oxX3P3//Pwly5S04IzNULkct/BVc0WoenrAu2o/Nad3hEuJCJlzCnTQBPSmD5Bs0QRUpad8k5nGgd+yDy5APdhrl0zj86Enx63B+Zd8qCgrFleGz6Z4xu3CI0r2/XM+90HVfukitaoxpCwHdPPE2JOrWIiIpi9Sdf0PzlF6hyd1t8bjfLJrzL1u9/pu3YEdR48D5O7wzs7L5o9yA+d9bOeb/SqW6WlvPfJVe6HAiB76PRiLIVIcKFuXhO4C45oWEs+RVzwU8A6G06gOHD+O2/u/DYe+ZylnNH9BmEVrYCCIF7/GvoFeLB6cL364/+bq6RU3BPHmndDed0EfHsULT8hcBuw/vTDHyLf8ty9ojSBf9RXq1zH0SpOBAC4/NxiDIVwOlCLp3nv0tOCIG54nfMxbPROjyJVv9W5InA3X/GpKFQrDR6597g88Gl8xhfTQw+9ZRZlJiozDul7X/lLjkhMP9ehFxxnbGl09OpY8tlzK8ngCcFUfdWtKZtrJ3z7s2Yv89Eu6cHotbNcDpwJ6bx0Zvgu8EB+h9e0+K/S05o1l1yy+dBZDRaxz7WzFF0XrQuzyCcLmTCZcyvxkGRkujPjoF92yH1WN1cMhu5bxta9+cRDmuG3pw+OXD6KzOZXU5w5Y63EmWt7eOrCYjS5a3ZjeW/Be6SExrmyj+QS+ZcdxlOHUMfOQ3On/bPQsrdmzHnfo24qzNaVeug2dy6Bvnr9HTjBEU/dTHzTum8J/vjzyHKlEcIgee9EWhxlcDpwlgQuPbHMWwi3o/eRh47hP2RZ9Bvbh50XZPnrQFZ2oE7qv0X33t45S45Iay75FYvBGcU2t09gmZfRK1boFBx/11you5tiDpNrWufTh5Bzvsqa0XTf1NoXblLTmjWXXKrF4ArNfuMNNlrN7Gyz/8Wisei9RwGBwMHQ+bK32HHun/0o/VXP0+3Ld2CyefzYbPZ8Hiu/SU7HI4b+sH/tGDKTUJVMIVaVgum3CDLBVMOy3LBlAv8o4IpF/mnBVOukhMXAWeHXHr95Y3IcsGUw/6rgimnhWlmKrtlVDClew1T06ZNWbRoEW3atEEI4Z/6FEKwYMGCbA+pKIqiKIqSW6VbMLVt25Z27drRtGlTOnXqRJUqVdLrqiiKoiiK8j8t3atFX375ZebOnUvjxo0ZP348nTp14ttvv8WdxetTFEVRFEVR/q0yvL3Gbrdz55138uGHHzJx4kQOHjzIbbfdFq5siqIoiqIouUKm38OUkpLCH3/8wY8//khiYiIDBw7MbBFFURRFUZT/KekWTKtWreLHH39k1apVtGjRghdeeIFKlSql111RFEVRFOV/VroF06RJk+jYsSPDhw+/4a8RUBRFURRF+V+UbsH01VdfhTOHoiiKoihKrqX+VoiiKIqiKEomVMGkKIqiKIqSCVUwKYqiKIqiZEIVTIqiKIqiKJnItGD69NNPOXfuXDiyKIqiKIqi5EqZfnGly+Wid+/eFClShPvvv59bb70VIUQ4simKoiiKouQKmRZMnTt3pnPnzuzevZv333+fYcOGcf/99/Pwww+TJ0+ejBf+FxdWBe16TkfIkrNeI6cjZJn4l65z81+8zqXv35ldGP/O3ADG+cs5HSFL9CIFcjrCf+FiTgfIEunz5XSELBP6v3M8z0imBdOlS5eYM2cOP/30EzExMbz00kv4fD569+6tvqtJURRFUZT/FzItmB544AHuvvtuxo8fT/Hixf3P79ixI6TBFEVRFEVRcotMC6bffvst6JqlU6dOUaRIEZ599tmQBlMURVEURcktMi2YJk2axNdff43X68XtdlO2bFnmzJkTjmyKoiiKoii5QqZfK7BkyRKWLFlCu3btmDt3LkWLFg1HLkVRFEVRlFwj04IpX758OBwOEhMTiY2NJTk5ORy5FEVRFEVRco1MC6ZixYoxa9YsXC4XY8eOJSEhIRy5FEVRFEVRco1Mr2F67bXXOH78OHfeeSc//PADEyZMCEMsRVEURVGU3CPdgmnGjBnXPOdwOFizZg3ly5cPaShFURRFUZTcJN2C6fTp0+HMoSiKoiiKkmulWzA9/fTT/n+vWLGCI0eOULNmTeLi4sISTFEURVEUJbfI9BqmcePGceLECfbu3YvdbufDDz9k3Lhx4cimKIqiKIqSK2R6l9zatWsZPXo0kZGR3HfffRw5ciQcuRRFURRFUXKNTGeYDMMgJSUFIQSGYaBpmdZYWSaq1kNr+SAYBubqRchV84M7RMagde2PsDuQl85hzngXvB5/s/bAk5CUgDl3Gug2tI59EAWLIt3JmD98BGdOhCy7/z0Iwd2TxlKsZjV8KR5+6PUM5/bu97fX7tqRps/1xX3xEuu+/Jq1n3+FZrPR/qPJ5I8tgy3CwaIRY9kxe17Is/5TZW+qT/tRwxnXrG1ORwEh0B/qiyhdDrxefF+Mh1PHAs21GqG36wqmgbnsN8wladZnTD7sr7yLd+xgOHEYUbocerd+YBrIk0cwPh8PUoblPTifGYxWrhJ4PSSPex15LHBAYmvWmoj7uiBNA3P/btwTR/pz6fHViXi8L0kDngx9zjR5s7LObcPeg6REAOSZExifjbXWeZc+YJrg8+L7ZDRcuhC66NXqo7XqAKaJuWoBcuUfwR2iYtC6PWeNLRfPYX4zCbweRM1GaC3agwTzr9+Dx6QyFdHbdcd4d2jIciMEtu7PIEqXB58X76djg9a5VrsR+t3dwDQwlv6K+edcAPS2ndHqNAabDWPhz5hLfoWYfNh6PIeIigZNw/vhKDh9PHTRq9RDu+N+a52vXoT8e0Fwh8gYtC7PpI7n5zFnvmeN56XKo7frDgjk5QuY0yeB4UN7oBeicHEwTYyZU+DcyZBlD7wJgf3x59BiKyC9Xrzvj0KePBrcxxGB4+XxeN8fiTx2CHQd+1NDEIWLIex2vN99ibl2eeizXi9+5Tpot99rfSbXLUGuXXz9fo1bI6LzYv4x0/+cdldX5JnjyNULwxM2rUq10W67G0wTuX4pct2f1+0mGrWC6LzI+d9aj6s3tJ6TJvLkEeScL7N1LM+0+nn44Ydp3749u3fv5sEHH6Rr167Z9sODk+hodz+C8eHrGFOGoTW6A2LyBXdp+SBy/VKM94Yij+63Vkwq0agloliZNI/vAI8bY9KLmD9+gnbf46HJfZUq97TF5ozgg1tb8/tLw2kz+g1/W2TBAtzx6kt8fMd/+LhFW2p1fpB8saWp3aUDSWfP8VHzNnze7kHaTRgdlqz/RKuB/ej28SRsTmdORwFA1LkZ7A58b/XH+O4TbB16Bhp1HVvHJ/GNG4Jv1AC0W9tAnvyBtu79wJMS6H53N4xfvsI38jmwORA1G4blPdhuuR0cEST160HKJ5NwPpnm7zM6InA+0pvEgU+S1P9RRFQ0tkZNraYO3XE+NxQcEWHJeUWW1rnNDoBvzEB8YwZifDbW6t65N8bX7+IbMxBz3XL0uzqGLrimo93zKMb7wzEmv4zWuOW1Y0urDsi1SzAmvWSNLTe3BqGh/acbxpRXMd4ZjNb8XoiKsdZF83vRO/bxv7+QRa97C9gdeN94Bt+3H2Pr1CvQqOvYOj+F9+1BeEc8h35bW8ibHxFfC1GxKt43++Ed8RyiQBEAbB2fwPxrAd4Rz+H77jO0EmXS+anZEVxHa/cwxsdvYrw/DK1hC4jOG9zljgeQ65dhTBmWOp63tN7WA09izHwPY8oryF0bIH8hRNX6ABjvvYL5+0y0dt1Dlz1txgZNwR5BystP4f36fezd+wS1i3KViRg+Ga1YCf9zetPWcPkinmFPk/LWQOyP5dDfXdV0tLu6YnwxCuPTN9HqN7vmd4DNjvZAL7SGdwSei4xB6zYAEV8nvHmv0HS0OztjTn0b8/MRiHq3XTe3aN8T0aB58HPN78f8YhTmJ29ChAsq1creaJl1uOuuu/j666/54IMP+Pjjj2nXrl22BvArWgp55gQkJ4LhQ+7fgYirEtRFxMUjd24AQO5Yj6hUw2qIrYSIrYiZ5qhRFC2F3LHeenD6GKJIydDkvkrszY3Y9bt1JHX47zWUrFvb31YgriwnNm0m+fwFpJQcXbue0g0bsOW7n5j/6lv+fqbPF5as/8Tpvfv5oP1DOR3DT6tYHbllDQBy3w5E2Ur+NlG8DPLUMUhKsLal3VsRlaoDoHfoibF4NvLCWX9/89AeRFQea1mnC4zwrH+9Wm18q1cAYGzfgl6paqDR6yGxXw9Icad2tiE91myqeewIycMHhCVjWllZ56J0eYQjAttzI7ANGI0oFw+A74O3kIf3pb6wFjRTnO2KlkKeOZ5mbNmOKFc1qIsoV8U/Xsjt6xCVaoI0MUb2BXdSaqEkAr+PMycwPhsVusxXclWsjrl5tZVr73a0uPTXubl7C1qlGmjV6yMP78fWdzj2/m9gblhp9a9QDVGgEPaBo9Ebt8DcvjF0wYuURJ69Mp4byAM7rzOeVw6M5zs3ICrUgMLFkYmX0Zq0Re/1Krii4fRx5NbVmN99YC2YvzAkXAxd9jT0+JqYG1ZZGXdvQysfH/we7A48b7+EefSQ/znjr0V4Z3wc6GQYYcl6jcIlkOdOWtuvYSAP7ULEVg7uY7Mj1y/D/PPnwHMOJ+aiH5AbcmZWjMLF4dypNLl3Q5lKwX1sduTG5cilswPPGT7MT97wjyVC08HnzdZoGRZMX331FV26dKFz585MmDCBRYsWZesPDxLhslbQFSnJ4IwM7uN0QXKSv104IyEmH1qrDpjffxzUVR49gKhSz3pQpiLkLQAidKcT/RHzxJBy8ZL/sWmYaLoOwJk9eylSJZ6oIoWxu1yUb3YrjshIPImJeBIScERH02X6F/zx6pshz/lPrf/+Zwxv9m58/xVnJDL1NA9gndq5crrYGYlMTtPmTkK4otBuaYm8fBG5dW3wa508it7lKexvfAJ58iN3hHBHkoaIiobENN+cb5qgWdsKUiIvnAPAfk9HhNOFsdba8fmWLUTmRFGdhXWOx43x2yxr5mnqO9ieGGwtc9F6b6J8VfTm92D8/n1IcweNLW73tWNLRJo+KckIZ5T1b9NE1GiEPnAcct9W/85PbloZlsJauCL9pzOv5PGvc1dU8O/DnQSuKERMXrS4SvjefQ3fFxOwPTnEeq1CxZCJCXjHvIA8ewq9bQhn9ZzXGc9dma3zSIjMgyhbGfOv3zA+fB1RoTqignWwg2mideiDdk8Pa/2HgysKmRT4jMq0n1HA3LkZefZU8DIpyeBOBqcLx3Ov45v+UXiyXu26+1RXcB93EnLvluDnLpyGI3tDny89ES5k2twet3Ugm5Y7CfZuDX5OSki09r3ipjusGfir+/yX0r2GadKkSZw+fZq33nqLQoUKcfToUT799FNOnjxJ7969sy2Admcn68ijeBnkoT2BhggXuBODO7uTwemEBI+1UpOTELVuRkTFoD/+kjXNbncgTh1Frl6IKFoK/anhyP074Mg+kGa25U6P+9JlHDHR/sdCE5ipg6z7wkXmDnyJLjO+5NLRYxxbv5Gks9ZMR95SJen67VRWvf8Jm6bPCnnOfz13EsLpwn92WghrZ+JvSzM4p+7o9TvuBSnRqtRBlCmP7bGB+CYNQ+/cG9/I55HHDqI1a4fe8UmMaZND/hZkYgK4ogJPCAGmEfQ44ol+aKXKkPTaCyHPk6ksrHN58qg1CwJw8igy4RLkLQjnT6M1uA2tbWe877wckhkD7a4uiHJVoHisdZTqz+a8dmxJSbLGHO+VsSXQLjevxNiyCq1zX0SD25F/h++aDpmcFFzcpV3nyYnBO0BnJCQlIBMuIY8fsmbTThyx3lNMPki8hLn+LwDMDSvR7++R7Xm11h0RZeOvXecRLitvWlfWuc+bupNMhKTL1rWmp6zrhOSujVCyHOyxdurmzHdhbl70vm9hvP0ceFMIqeREq2hNJa7+jKZDFCyCY8Cb+H7/AWP5/Ez7ZyetxQOI2EpQtDQybeFzdQGVy4jm7RFlKkHRUnBkX2CccTiDC6gMX0QgWnZAFCyGOTP7x/B0p1yWLVvGa6+9RtmyZYmOjqZy5cqMGDGCFStWZGsA89fpGFOGYbz6OKJgMWsKVrdZU+QHdgX1lQd2IOLrAiDi6yD3b0cum4sxYRDGlGGYC39Arl+GXLMYSldA7t9uPb/l72uPAkLk0F+rqHyndS6+9E31Obllu79N03VKN6zPx83bMKtHLwpVrsTBFauIKlKYR+Z+x68vvsraL6aFJee/nblnK6LmTQCIcvHIowf8bfL4IUTRktZpFN2GqFQDuXcbvlHP4xs9AN+YgchDe/F9MgYunYfEy9aOCaxZncjo6/3IbGds3Yit4S0A6FWqY+7fE9Tu7P8SwuEgedjzgVNBOSgr61xr0hq9Y+qF6fkKWLNOF8+iNWqB1vxufGMGhuxmDHPe1xjvDsV4pQeiUDHr96rbEOWqIQ/sDOor9+9AVEkdW6rURe7bBhEu9D5vgG6zjl49KeG5GSBtrj1b0WqlrvPyVZBHAjeQXL3Otco1MPdsQ+7ajFa9gdUpX0FEhBMSLmHu2uJ/La1yDeSxg9me1/xtBsYHwzFee8Ja564o0HVEXBXkwavH853+62RE5drWge25kxDhhIJFrefLxsPJw4i6TRHN7rUW9Hqs30MYDoCNnZuti+cBUbEq5qF9mS+UNz+Ol8binfY+xqK5IU54LXPBLIxP38IY9TSiYNHA7yC2cvCkRC4jF36P+flIzDH9oECRoNwcvrHc4j+PgM2OOX1iSE7zpzvD5HA4rnlO0zR0Xb9O72xgGpi/fI7e82UQAvPvRXDpHLii0To8hfnFGMz536F1ehqt4R3IxMuYX09I//VOH0e07oR2291Id5J1B0YYbPtxNhVaNKPnn78hBHz3xNPU7PQAEVFRrP7kCwyPh96rFuNzu1k24V2Szp6j7dgRuPLlo9mLA2n24kAAvmj3ID53zu8kcyu5bjlUrYttyHgQAt+nY9EaNoMIF+aSufhmfIDt2bdAaJjLfoU01yxdzff5OGxPvmgdOfp81t1fYeBbvghbvYZETvgUhMD99nBsze5EuFwYu7Zjv/MejC3riRzzPgCeH6bjWx7C0+KZyMo6N5f+iv7oAGyDx4GU+D4bCxL0Lk8hz57G1vsV67V3bcL4aWpogpsG5k+foT/5ipVt1QLrlGBkNFrHPpifjcL8/Vu0Ls+gNW6JTLiM+dU48KRgrvsTve+b1rUUxw4g11z/bp1QMdcuQ6tWF/tL71jr/JMxaI2aW+v8zzkY09/H/vxI0ATG0tR1fuEsonJN7K+8C5rAO3USSBPf9Pex93gevVk7SE7E+/5bmQfIcnAD85cvrZl/oWGuXmQdnLii0B7ohTl1LOaC79E69kFr2CJ1PJ9o3SH97RT0zv1AgDy4y7q2zB6B1qE3Wq9XQbdh/vx5tl+fct238fcS9Jr1cbz+HkIIPO+NQL/lDnC6MBb8ct1l7Pd1Q0THYLv/Ybj/YQA8bw0I7XV612MamPO+Ru/+grVPXbcELqf+Du59DPObieHNc6NMA/O36WgPPQ9CQ65fCpcvWLnv7oE5I52Zo+KxiLpN4eAuxMODrJda+TvsWJdt0YSU1z9k6t69O19++eUNP389vgEP/HfpctCwiQsy75QLnfXm0AWG2WDio41yOkKWuA+lX4zlds4yBXM6QpZoeaIy75RLGecv53SELNGLFMjpCFnmPRC6r08IJXvlsjkdIctEqCZXQkx/9fN029KdYVq3bh1NmjS55vmLF8Nzd4KiKIqiKEpukW7BtGXLlvSaFEVRFEVR/l8J/X32iqIoiqIo/3KqYFIURVEURcnEPy6YTp8+HYociqIoiqIouVa6BdPWrVvp1asXgwYN4tw561t5p02bRvv27cMWTlEURVEUJTdI96LvoUOH8txzz3Hs2DHGjx9PUlISp06dYto09cWKiqIoiqL8/5LuDJPL5aJJkyZ06NCBJUuWUKpUKb788kvKlAnhX7hWFEVRFEXJhdKdYUr7jd5FihTh2WefDUsgRVEURVGU3CbdgklKidfrRUqJ0+n0/xuu/2dTFEVRFEVR/lelWzAdPXqUO++8018ktW7dGrD+WvOCBf/OPxuiKIqiKIqSFekWTAsXLgxnDkVRFEVRlFwr3YJpyJAh6S40YsSIkIRRFEVRFEXJjTL8W3Jut5u7776bOnXq+E/NKYqiKIqi/H+T7tcK/PLLL7z77rukpKTw4YcfsmHDBsqUKUPTpk3DmU9RFEVRFCXHCXmDU0erV69m6tSpnDhxgpkzZ97Qiyfed8t/FS4n2WKcOR0hS4Rdz7xTLvXMpytzOkKWTH72jpyOkGW+U+dzOkKW2IoWyOkIWSYKFcrpCFmSuHBNTkfIsg2bTuZ0hCy5ZWinnI6QZaLev3NyRWt8T7pt6Z6SuyIhIYE//viD2bNnk5yczN13352t4RRFURRFUXK7dAumefPmMWfOHI4dO0arVq0YPnw4pUqVCmc2RVEURVGUXCHdgunZZ5+lXLlyxMfHs2vXLsaPH+9vGzt2bFjCKYqiKIqi5AbpFkxffvllOHMoiqIoiqLkWukWTDfddFM4cyiKoiiKouRa6X6tgKIoiqIoimJRBZOiKIqiKEomVMGkKIqiKIqSCVUwKYqiKIqiZEIVTIqiKIqiKJlQBZOiKIqiKEomMiyYXnvtNf+/t23bFvIwiqIoiqIouVGGBdOePXv8/x45cmTIwyiKoiiKouRGGf7xXSnldf8dckLgeHIAWtkK4PWQ8u5I5ImjwX0cEThfnUDKuyOQRw8Fns+bD9fbn+J+tX/w8+EiBLaH+yHKlAevB+8nY+HUMX+zVrsx+r0PgWliLJmHuXguWpPW6E1bWR3sDkSZCnieeQCSEkOeVX+oL6J0OfB68X0xPiirqNUIvV1XMA3MZb9hLpkXWDYmH/ZX3sU7djCcOIwoXQ69Wz8wDeTJIxifj4dwbjMZKHtTfdqPGs64Zm1zOgoAomp9tFYdrPX69wLkyvnBHaJi0B56FmF3IC+ex5w+CbweRM1GaM3bAxLzrz+Qq+aDpqN16YvIXwSkiTFzCpw6et2f+98HF9ge6Y9Wpjz4vHg/HoM8mWbbrtMY233dwTAw/pyHsXgO6Dr2J4cgChUFaeL9+G3k8cOIshWx93gWfF7Mg3vwTZ0c0u1FVK2P1vLB1HW+0Fp3aUXFoHXtb63zS+cxp08Gryfw3h7oBckJmHO+sl6v+X1o1RqAbsNc8Rvy7wUhyx6kQk20Jm3BNJEblyM3LrtuN9GgBUTlQS7+AaLyoN3zeKCxaGnk4h+Q65eEJ3NQMIHzmcFo5SqB10PyuNeRx474m23NWhNxXxekaWDu34174sicHUeEoMKot4iuVhUzxcOu5wbiPnDA31zyySco1qUT3rPnANg9cBB56tejaMcOAGjOCKKrVeWvGnUxLl0Ka/RF+08w5e9d6JpG+yqlebB6bFD7sctJvDx/I4aUSCkZ3rwWcfmj+Xz9Xr7bdogCrggAXm1Wk7j80eHNvn4b7/0838retAEdbm8Y1H4hIYm7Bo+mYsliANxRrzrdWzVh877DjJr+C1JCobwxjO7ZiQiHPdtyZVgwCSGu++9Q0xveCnYH7sFPolWqhqNHX1JGDPa3a+XjcfQaiChY+KoFdSJ6vQCelLBlvZpW7xawO/C+1hdRvgq2Lr3wTXjFn8/W9Sk8w3pDihv70Hcw1/9lFSPLfgPA1v0ZjCW/hr5YAkSdm8HuwPdWf0S5eGwdeuKb/Goga8cn8b7RF1Lc2IaMx9ywEi6dt9q69wtaz/rd3TB++Qq5eTX6E4MRNRsiN64M+XvITKuB/WjYrRMpiUk5HcWi6Wj39sAYb22net+3MLaugcsXAl1adUCuW4q5ehGi+X2Ixq2QS+eitX3IWi7FjT7oHYwtqxBl40HTMSa9iKhUC61NF8zPx4Qmer0mCLsDz/CnU7ft3njHv2w16jq2h/rgGdoLUtw4hk3CWL8CrXxV0HU8r/VFq14P24OP4504DPujz+OdOgm5eyu2Bx5Fu7kF5vL5GQfIcnAd7Z5HMCYMstb5029ibLtqnbd8ELl+WfA6XzIbANGoJaJ4GeQ+67IEUb4aomw8xuSXwB6BdvvdhGWXrmlodzyI+fkI8KSgdX8BuWcTJKbZEdvsiLu6IUqURe5cbz2XeAnz63HWv0uWQ7v1HuSGpeFIfA3bLbeDI4Kkfj3Qq1TH+eSzJA973mp0ROB8pDcJPTtCihvXi29ia9QU3185UNilKnjXnWgREWxoew8x9epSbvhQtj38mL89umYNdvbtT8Kmzf7nkvfu4+SMbwGoMOINTnwzI+zFktcwGbl0KzM7NMVlt/HQrGXcHleUwlFOf59JK3fSpWZZ7ihfnGUHTzF+xXYmtm3AttMXGdmyDtWK5AtrZn92n8HIb35h5rC+uCIcdH3zPZrVrkrhfDH+PtsOHqVtw9q83O1e/3NSSl75bBYTnu5GbNFCfPvnKo6dPU9c8SLZli3DU3Lr1q2jSZMmNGnSJOjfTZo0ybYA16NXqYmx3trZmru2opWPD+5gt5Mycgjy6MGgpx2PPI3vtx+R586ENF9GRKUamJtWAyD3bkcrWznQViIWefIoJCWA4cPctQWtUo1Ae1wlRMlYzMVzwpJVq1gduWWNlXXfDkTZSoEsxcsgTx3zZ5W7tyIqVQdA79ATY/Fs5IWz/v7moT2IqDzWsk4XGL6wvIfMnN67nw/aP5TTMQKKlkKeOQHJidZ63b8dUa5KUBcRVwW5w9rZyR3rEZVqWbNHo54BdxJExQACUtzI08dA00EIcLrAMEIWXatcA2PT31auvdvR4tJsL1dv2zs3o1WuiTxxGDTNyueK8m8XokBh5O6tANd8DrLd9dZ5XAbrfPs6RMWaVkNsJURsJcyVfwT6Vq4Nxw+iPfIC2mNDMLetDV32tAoWh/OnrW3ANJCH90DpCsF9bHbklr+QK+Zd9yW0lp0wf/s6x2Zt9Gq18a1eAYCxfQt6paqBRq+HxH49IMWd2tmG9Hiu8yrhk7dhA84vWgzA5bXriKlVK6g9pmYNSj/zNLV+/p7Sz/QJaouuVZPIypU5MXVauOL67TufQGzeKPI6HTh0jbolCrD22LmgPi80qcptZYsCYJiSCJsOwLZTF/lozR4emrWMD9fsDn/246coU6QgeaMicdhs1K1YlrW79gf12XrgCNsOHqXbiCn0nzyVUxcuceDEafJFR/Hl78voNmIKFxOTs7VYgkxmmNasWYPT6cyoS2i4ooJnWEzD2imY1s7A3LH5mkVszdogL17A2PA39vu7hSvpNYQzEpmcJrs0rB2GaYLrqjZ3MkQGpjr1dl3w/Tg1fGGdkcig9WwGsl79PtxJCFcU4paWyMsXkVvXQptOgfaTR9Efehr9P12QyYnIHRvD9z4ysP77nykYWyanYwQ4XZCcZrYrJRmcUdf2caf2cScjnJHWv00TUaMh2v09kdvWWsWRx40oUAR90CSIjsH4+K3QZXdFXvW5NIO27aA2dzIiMgrTnYwoXAzH6C8QMXnxjH0RAHnqGCK+FnLHRrS6NyMiQjjOpF2fYO2QXZHX9rnye0lxI1yREJMPrXVHzM9GIWrfEugbFQP5C2N+MgIKFEF/dLBVzIZahBPpTg489rgREa7g2S13EuzfDjUaX7t8hZrIM8fg3MlQJ02XiIqGxITAE6YZGNulRF6wdur2ezoinC6MtTk7S63HxOC7dNn/WBoG6Lr/wOTUjz9z7LPPMS4nUPWzjynQcgfn/rBOz5bp15eDY8fnSO4Ej5foNKeiouw2EjzeoD75U0+57T+fwJjl25jUtgEAd1UsQZeaZYly2HlmzmoW7z/J7XFFw5c92U10ZGA8iHJGcDk5OahPueJFqFa2FDdXq8gvK9bx5lc/8XDrpqzfc4CXHrqH2KKFeGrCZ1QrW5LGVStmW7YMC6bBgwcjhKBhw4bcfvvtFCtWLNt+cIaSE8GZZkATmr9YSo+tRVtAoteqjxZXkYh+Q0l5a5D/Axgu0p1kDb5XiNQdClgDctr35XRZR+QAkVHWrM72DWHLijsJ4Uwz4AoRyOpOCuyowV9c6XfcC1KiVamDKFMe22MD8U0aht65N76RzyOPHURr1g6945MY0yaH773kctpdna1ZjRKxyINpjtoiXNb2npY72Xre6wGnK6hwlZtXYWz5G61TX0T9261tZud6zDnTIF9B9KeGY4yxrg3KdslJwYWGdvW2nWa7d7qQiQnY7noQc9NqfDM/hgKFcbw4Ds+QR/F+NBpbt6fhP52Q+3Ygvdk/k6Dd2RkRF3+dde68/jp3OiHBYxUmyYmIWjcjImPQH38J8uS3ri88Zc2iyVNHrdmy08esdR2dBxJCc9pF3HoPolR5KFIKju0PfF4dVxVQmb1O9YbI1QtDkvFGycQE64D4CiGCx3YhiHiiH1qpMiS99kL4A17FuHwZPTqQV2ha0Czu0Q8/xrhsFVTn5i8gunp1zv2xAD1PHlwVynNx+Yqw5n3nrx2sO36OnWcuUbNoPv/ziV4fMRHXXsuz6sgZXl+8mZEt6xCXPxopJd1rl/P3va1sUbafvhiWgmnCd7+ybtcBdh05Ts1ygYPcRHcKeSJdQX0bVSmPM8IBWNcvTfrhd/JFRVKmaCEqlLSyNqlRia0HjmZrwZThKbkJEyYwatQoihcvzocffkjv3r2ZMGECGzeGdvbA2L4ZvZ51hKRVqoZ5aG+my7hf7oP75adxD+2LuX83Ke+8HvZiCUDu2oJWy7pATZSvgjwcmEqUxw4iipa0jlB1G1rlmph7rOsitMo1MbeGaWo/lblnK6LmTVbWcvHIowcCWY8fCsoqKtVA7t2Gb9Tz+EYPwDdmIPLQXnyfjLGua0q8jEw9QpcXzgXNnClgzvsG471XMF55FFGomLV+dBuiXFXkwZ1BfeX+HYgqdQEQ8XWQ+7dDhAu9z+ug26zTKR43SNOazbsyM5KUYLVrofl6NXPXFvQ027Z5eF8g87GDiGKlAtt2fC3MPduQiZcDBV/iZYRus64pqt0I74ej8b49BKLzYG7J/m3f/PUbjCnDMIY9hihUHFxp1vmBXUF95YEdiCr1rPdWpS5y33bksrkYE17AmDIMc+EPyPXLkKsXIfdtR8TXsRbMkx8cEcGzJtlMLvkJ8+txmBMHQP7C1kGXpiNKV4Sj+zJ/gVSiWCwczXwsDSVj60ZsDa3ZOr1Kdcz9e4Lanf1fQjgc1nVNV07N5aBLf6+hQIvmAMTUq0vi9h3+Nj0mhvp/LkCLtA4i8jW5hcup1zLlbdyQC0uvf0F+KPVrHM8X7W9m6WOtOHQxiQtuDx7DZM3Rc9Qulj+o76ojZxixZAsf3N2Q6qnFVYLHxz1fLybR40NKyaojZ6haJG9Ysve//06+HNKLpe+8wsFTZ7iQkITH52PNzv3UrhB8wfrLn83i9zXWul65bQ/VypaiVJECJLlTOHjSuiRn7a4DVCiRvYVehjNMQ4YMCXqcN29e9uzZwyeffMLmzdeeFssuxqo/0Ws3wDnifRCClElvojdtiXC68P3xc8h+bnYw1y5Dq14P+9CJIAS+j0ajNW4OES7MxXMwvn4f+8CRIDTr4u7z1i9XFC8Np4+HNatctxyq1sU2ZLyV9dOxaA2bWVmXzMU34wNsz74FQsNc9iukuWbpar7Px2F78kXraNHns+64U65lGpg/fY7e8xUQAvPvBXDRKjC1Dr0xPx+N+ce3aF2eQWvUEpl4CfOr8eBJwVy7BP3pN8AwkMcPItcuAbsDrVMftKffsO7YmjstZDc9mGuWolWvh+OVSSAE3g9HoTVuYZ06WTQb37T3cAwabW3bf86D82cw5n2Lvecg9KHvgG7HO/Nj69qrE0dwDBwJKW7M7RswN64KSWYruIH58+foPYda63z1Qrh0DlzRaB2ewvxiDOYfs9A690VreIe1zqdNSPfl5Pa1iPJV0fuNsl7v+49BmqHL738fJuaCWWid+gECuWkFJFwAZyRam+6Y37+f/rKuaKvIzmG+5Yuw1WtI5IRPQQjcbw/H1uxOhMuFsWs79jvvwdiynsgx1nvx/DAd3/JFOZb3zNx55LutKbVm/4gQgp39nqNw+3vRo6I4MXUa+98aRa3vZ2J6PFxYupzzC6wZvMjy5XEfPJjJq4eOXdcY1LQqPX9aiSmhfdXSFI12ccHt4ZUFG5nYtgEjl2zFa5i8OH8DAGXzRTG8eS36N46nxw8rcOgaDUsV9l/nFLbsNp3BndrxxNiPMU1J+6YNKJo/LxcSkhj62Swm9e3O8w+24aVPZvLNgr9wRTh4/dEHcNhsvPHogwx8/xskkjoVYrm9dpXMf+A/IGQG3xfQrl073G43d999N3Xq1An6aoGmTZtm+uKJ992SaZ/cyhaTA9duZQNh13M6QpY982nO31WXFZOfvSOnI2SZ79T5nI6QJbaiBXI6QpaJQoVyOkKWJC5ck9MRsmzDppy7buu/ccvQTpl3yqVEvcxrhNxIa3xP+m0ZLfjLL7/w7rvvkpKSwocffsiGDRsoU6bMDRVLiqIoiqIo/ysyPCUHUKlSJQYMGADA6tWrGTt2LCdOnGDmzJkhD6coiqIoipIbZFowASQkJPDHH38we/ZskpOTufvuu0OdS1EURVEUJdfIsGCaN28ec+bM4dixY7Rq1Yrhw4dTqlSpcGVTFEVRFEXJFTIsmJ599lnKlStHfHw8u3btYvz4wJ1PY8eODXk4RVEURVGU3CDDgunLL78MVw5FURRFUZRcK8OC6aabbgpXDkVRFEVRlFwrNF8JrCiKoiiK8j9EFUyKoiiKoiiZUAWToiiKoihKJlTBpCiKoiiKkglVMCmKoiiKomRCFUyKoiiKoiiZUAWToiiKoihKJoSUUobqxT2PtQrVS4ec5/iFnI6QJabXyOkIWRZZIzanI2TJ0+Pn53SELJvcv0VOR8ga7d97rGeeu5TTEbJEyxed0xGyzLyclNMRskR/qEdOR8gy+fPMnI6QJbZx36fb9u8ddRRFURRFUcJEFUyKoiiKoiiZUAWToiiKoihKJlTBpCiKoiiKkglVMCmKoiiKomRCFUyKoiiKoiiZUAWToiiKoihKJlTBpCiKoiiKkglVMCmKoiiKomTihgqmAwcO8Oeff3LixAlC+MXgiqIoiqIouZItsw5fffUVf/zxBxcvXuTee+/l0KFDvPLKK+HIpiiKoiiKkitkOsM0Z84cPv/8c2JiYnjkkUfYuHFjOHIpiqIoiqLkGpkWTFdOwQkhAHA4HKFNpCiKoiiKkstkekqubdu2dO3alWPHjvHEE09wxx13hCaJEOgP9UWULgdeL74vxsOpY4HmWo3Q23UF08Bc9hvmknmBZWPyYX/lXbxjB8OJw4gyFdC7PQM+L/LwXoxvpkC4rr0Sgog+g9DiKoLXg/udN5HHjwT3iYjA9eZk3BPeQB45CLpOxPOvohUpDqaJe+Kb1vPhJATOZwajlasEXg/J415HHgvktjVrTcR9XZCmgbl/N+6JI/3rVI+vTsTjfUka8GR4I1etj9aqg7VN/L0AuXJ+cIeoGLSHnkXYHciL5zGnTwKvB1GzEVrz9oDE/OsP5Kr5oOloXfoi8hcBaWLMnAKnjob1/VxP2Zvq037UcMY1a5vTUQAQ1a6scxNz1QLkyj+CO0TFoHV7LnWdn8P8JnWd12mCdls7ME3k8YOYsz4AoaF1eQZRIHWdz3gvZOtcVK2P1vLB1G1lofU7vzp31/5W7kvnMadPBq/H36w90AuSEzDnfIVo0Ayt/u1Wg90BJcpivPoYuJNCEFygd3vGGhd9Xnyfjbt2XLznITAMzKW/+sdF26tTIDkRAHn6BManb0NMPmw9noXIaNB0fB+NgtPHsz/zlWzZua1IiWjRHq36TaDbMJfPQ65aEKLgAr1rX0TpOGudfzHhqnXeEP0/V/ZFv2MuTbsvyot96Lt4xw2x9kWly6F37gPSsPZrn46BSxdCk/sqizbuZMqcxeiaRvtb6vBg0/pB7RcSk2gzdBIVSxYB4I7a8XRr0Zg5f2/mywV/oWsalUoV5ZXObdG00N8flq3jOaA/97b/MynPnbI+0/+lTAumbt26cfPNN7Nr1y7KlStH5cqV/+sfej2izs1gd+B7qz+iXDy2Dj3xTX7VatR1bB2fxPtGX0hxYxsyHnPDSrh03mrr3g88Kf7X0h/uj/H1e8i929DvewStYXPMlSH6cF1Fb3wb2B0kP/8YWuXqRDzeD/frA/3tWsUqRDw9GFGwSGCZBreArpM84HH0OjcR8fBTuN8cHJa8V9huuR0cEST164FepTrOJ58ledjzVqMjAucjvUno2RFS3LhefBNbo6b4/lqCo0N37He0RbqTw5oXTUe7twfG+BfAk4Le9y2MrWvg8oVAl1YdkOuWYq5ehGh+H6JxK+TSuWhtH7KWS3GjD3oHY8sqRNl40HSMSS8iKtVCa9MF8/Mx4X1PV2k1sB8Nu3UiJTEEO+Ks0HS0ex7FGD/QWufPvIWxdfW163ztEmudt2iPuLk1csVvaG26YozuB16PtZOsWh+EAF3HmDgkdZ13xfx8dIhyP4IxYZCV++k3MbZdta20fBC5flnwtrJkNgCiUUtE8TLIfdsAkKsXYaxeZC3X/nHk3wtDUywBou4t1rj4Zj9EuSrYOj2Jb+Iwq1HXsXXuhfe1p61x8aUJ1riYlACAb9SAoNfSOzyB+dcCzNVLEPG1EMVLI0NVMGX3tuJOQsTFY0wcAvYItGb3EKpDYGtfZMc34llrX/RgT3zvvmo16jq2jr0C+6LB4zA3ptkXdbtqX9TpKYxv3kUe3od2axv0OztgzPwwRMkDvIbByG9/ZeaQnrgi7Dw0+hNur1mZwnlj/H22HTpOmwbVeblz4GDM7fEy8acF/DisNy6HgwEff8vizbtoXis+tIGzeTwnxQ2A8V72Xm+dadk4ZMgQPv74Y5YsWcLnn3/OK6+8wnvvvcfFixezN0jF6sgtawCQ+3Ygylbyt4niZZCnjlkDgeFD7t6KqFQdAL1DT4zFs5EXzgb65y+E3GsNbuburYiK1bI1a0b0arUx1v5l/eydW9AqVgnuYLfjfn0g8sgB/1Pm0UMITbd2IJFRSJ8vbHmv0KvVxrd6BQDG9i3olaoGGr0eEvv18G+E6Dakxzr6No8dIXn4gKtfLvSKlkKeOWEdRRs+5P7tiHLB61rEVUHuWA+A3LEeUamWNZMx6hlrBxcVAwhIcSNPH4MrvwOnCwwj/O/pKqf37ueD9g/ldIyAoqWQZ45ftc6rBnUR5dKs8+3rEJVqgs+L8c7gwIyNpoPPY32mg9Z5iLb7620rcRlsK9vXISrWtBpiKyFiK2FePTsCUKo8omjpa2dOspFWsRpy82or177tGY+Lu7YgKtVAlCmPcERge34kthdG+z8XWsVqkL8wtgGj0Bq3QO7YFLLc2b2tiPg6cOwgWo/BaI+/iLltTciiaxWqXbUvqhjIfPU637MVUTF1X/TgExh/zkFeDOyLfB+OQB7eZz3QdfB6Q5Y7rX3HTxNbuAB5o1w4bDbqVijD2j2HgvpsO3iM7YeP0/3tT+n/wQxOX7yMw6YzbdDjuFIvvfEZJhH2TOdV/nvZPJ5Toiw4ItCefAXtqeEQW+nan5kFmRZMKSkpFClShDZt2lCyZElOnjyJx+Nh0KBB2RLAzxmJTEoMPDZNuDIN6IxEJqdpcychXFFot7REXr6I3Lo26KXk6eOISjUA0Go3gghn9mbNgIiMQqYe4QGp70MPPNy2CXnmVPBCyUmIosWJ/PBbnM+8iPfnGWFKGyCioiExndxSIi+cA8B+T0eE04WxdiUAvmULc6TAw+mC5DRH9SnJ4Iy6ts+VI393MsIZaf3bNBE1GqIPGGfNGhgGeNyIAkXQB01C6/AU5tI54XkfGVj//c8YYRpgb4gzMngmxe22nksrIk2flGSEM8o6dZtgHWCJpm0gwoncuRE8yYgChdEHT0br0Dt06zztdgDWgOqKvLbPle0pxY1wRUJMPrTWHTG//+i6L6u1aI/5+7ehyXyFKyp47Es7LrquHheTEZFR4HFj/PotvrGD8X3xDrYnB1vLFCwKSQn43h6EPHsKvU3H0OXO7m0lKg+UqYD5xRjMb99Hf+jZ0GW/er1muC+y1rl28/X3RVy0xk1Rvip687sx/vg+dLnTSHCnEO2K8D+OckaQkOwO6hNXrDB92jXjywGP0qJ2Fd6cPhdN0yiUJxqArxauJCnFw81Vyoc+cHaP594UzMU/YX7wGuas99G79g/8Dv8LmZaO586dY9y4cQA0bdqURx99lP79+9O1a9f/+ocHcSchnK7ANKsQ1obqb0vzYUstrvQ77gUp0arUQZQpj+2xgfgmDcP36VhsnZ+Cuzog9+8KW1UPIJMSEa40v2hNgJnxbIX9vi4Y61bi+fw9RKEiuEa8R1LvLkHXUISaTEyAtLnFVbmFIOKJfmilypD02gthy3U17a7O1uxAiVjkwd2BhgiX/5oNP3ey9bzXA05X0EAnN6/C2PI3Wqe+iPq3W0eOO9djzpkG+QqiPzUcY8yz4MtFBUsO0e7qYh3tFY9FHkqzzp1OcF+1zlOSAus8Is06FwKtXXcoXALzs1HW6952N3LHBsw5X1nrvPdrGKP7Z9s61+7sjIiLv8624rz+tuJ0QoLH2kknJyJq3YyIjEF//CXIkx/sDsSpo8jVi8AZiShSEnPvlmzJmq7kxPTHxeSrx0UXMikBeeIo8mTqNTcnjyITLkG+gpB4CXO9NYssN/yFdv+j2R43VNsKSZeRp45Ys5Cnj1nLROf1F1fZKnW9pr8vcqV5X9Y611vca+2LqtZBlA7si7h0Hq3BbWhtO+F9Z2ho8qbxzo8LWLf3EDuPnKRmXEn/84nuFGJcwRMHjeLjcDrsANxRJ57JPy8EwDRN3v7+Dw6ePMs7vTr6b/gKhVCN53LdEmvGCqzr9JIuW5/hNGeispQ3sw4JCQns3bsXgL1795KUlMT58+dJSsrec/bmnq2ImjcBIMrFI48e8LfJ44cQRUtaU266DVGpBnLvNnyjnsc3egC+MQORh/bi+2SMtYHWaojv87H43hkK0TGY29am81Ozn7FtI3r9mwHQKlfHPLA302VkwiWrYAHk5Utgs2VLNfxPGFs3Ymt4CwB6leqY+/cEtTv7v4RwOKzrmlLc13uJsDDnfYPx3isYrzyKKFTMuoBVtyHKVUUe3BnUV+7fgahSFwARXwe5fztEuND7vA66zTqa9bhBmsjkROSVI5ykBKs9zL+D3Mqc9zXGu0MxXulx1TqvhjyQwTqvUtd/3Y/24FNgc2B+OtJ/ICCTEpDu0K1z89dvMKYMwxj2GKJQcXCl2VYO7ArOfWAHokq9NLm3I5fNxZjwAsaUYZgLf0CuX2YVS1gzBnJ3CE9pXXkPu7ciaja0fma5Ksgj+wOZrx4XK9dA7tmG1rQ1eqfUGzDyFbRmyy6cRe7agnbltSrXDBpjsy1vqLaVfdut03Jg7fgcTki8nO35Acw92xA1Gli5rrcvKnL1vmi7fz/kG/MC8nCafVGj5mjN7sY35gW4sgMPoX73tuCL53uw9O2BHDp9jguJSXh8PtbsPkjtcqWD+g798id+X2et85Xb91M1tgQAr077BY/Xx6SnOvlPzYVKqMZz0bAF2t2PWAvmyW8VWpfO/9d5hczkq7s3bdrEq6++yqlTp3A6ndx3333ky5ePQoUK0bp16wxf3PNYq3+QJPUuuVJxIAS+T8eixVaACBfmkrmBu+SEhrnsV8xFvwQtbhs4Bt/UidadCbUaod/7MHjcyB0bMX74/MZzXMl+/MI/XubK+4joMwitbAUQAvf419ArxIPThe/XH/3dXCOn4J480robzuki4tmhaPkLgd2G96cZ+Bb/lqUfb3qzeO3Nlbvk4ipaud8ejlYhHuFyYezaTtS7UzG2rPffGef5YTq+5ak7j6LFcb00gqRnHsnaz04VWSP2n0W+cleFENZdFct/hcho6/TO56MhOq91F1aEC5l4CfOr8eBJQTRqidawBRiGdRfO9x+D3YHWqQ8iT37rLpylc5Drlt5QjqfHz8+8UxYVjC3DY9M/Y3TjFiF5/cn9/9nr+u98Epp159PyedY679jHmg24ss6dLmTCZcyvxkGRkujPjoF92yH1uN1cMhu5cyNa56cD63zJ7Bte5/+0sPLfJScE5uqF1rbiirZOv34xxsrduW9gW5k2IejiXdGgmTWjNOcr6/Ht91jXWmThNKJ57tI/CH7lLrk4QOD75G1rbIlwYf45N3CXnBCYS3/DXPgz6Db0xwdadx8iMb79GLlnGxQsgq3Hc9YMW1Iivg9G+C8QvxFavuh/9D6zdVvZvAqtXXdEherW6835Crlzww1nMS//gwP8K3fJlYoDAb7PxqGVqQBOJ+aSeYG75DTNumP7mn3RaHxTJ8HJo9gnzESePQXJqQfEOzdj/Dz1hqPoD/W48dxXuXKXnCkl7W+uQ5dmDbmQmMQrX/7MxKc6ceTMeV7+4kck4HLYeb37PZy+eJkH3/qQehXK+GeWujVvxB11qmT8w65D/jzzH/XP1vFc06yxJV9hQGLMngpXFezpsY1L/7RppgUTWEXTV199xfLly2nduvUNf9P3PyqYcpksF0w5LMsFUy7wTwum3CKUBVOo/dOCKdf4F8/+/aOCKRf5pwVTbvKPCqZc5L8pmHLaPy2YcouMCqZ0r2HyeDzMmTOHadOm4XA4SEhIYMGCBTid4buAWlEURVEUJTdI9zCtefPm7Ny5k7fffpuvv/6aIkWKqGJJURRFUZT/l9KdYerevTuzZ8/m6NGjPPDAA9zAmTtFURRFUZT/SenOMPXs2ZOff/6Zbt26MXv2bLZs2cKYMWPYtWtXeosoiqIoiqL8T8r0ysmbbrqJMWPG8Mcff1CsWDFeeCHnvoNHURRFURQlJ9zwrSZ58uShW7du/PjjjyGMoyiKoiiKkvv8e+/NVRRFURRFCRNVMCmKoiiKomRCFUyKoiiKoiiZUAWToiiKoihKJlTBpCiKoiiKkglVMCmKoiiKomRCFUyKoiiKoiiZUAWToiiKoihKJtL9W3LZQSteJJQvH1IRNj2nI2SJ9Bk5HSHLfKfO53SELJncv0VOR8iypycsyOkIWTJl35KcjpBlyb0ez+kIWRJZoWxOR8iyxL9X5nSELIn5/uucjpBlomLFnI6Q7dQMk6IoiqIoSiZUwaQoiqIoipIJVTApiqIoiqJkQhVMiqIoiqIomVAFk6IoiqIoSiZUwaQoiqIoipKJTAumZcuWIaUEYMeOHSxZ8u+9nVdRFEVRFCUrMiyYvv76ayZPnkxiYqL/uXfffZcZM2aEPJiiKIqiKEpukWHB9MMPP/DFF18QHR0NQHx8PJ9++ikzZ84MSzhFURRFUZTcIMOCyel0EhEREfRcVFQUUVFRIQ2lKIqiKIqSm2RYMNntds6dOxf03Llz5zCMf++f31AURVEURfmnMvxbcr179+axxx7j3nvvpXTp0hw/fpxZs2YxcODAcOVTFEVRFEXJcRnOMNWvX5+JEydy+fJlFi9eTEJCApMnT+bmm28OVz5FURRFUZQcl+EM07Fjx9B1nfbt2yOEICIiggIFCoQrm5+oXAet2X1gGpjr/kSuWXz9fo1bI2LyYf4e5rv4hEDr3AdRuhx4vRhTJ8Dp44Hmmg3R2nax8i//HbnsV9B09IefhYJFwWbHnPsNctMqKF0eW59XkaeOAWAumYNcE6KvchAC/aG+/ty+L8ZD6s8FELUaobfrauVe9hvmknkA2Ia9B0nWnZPyzAmMz8YiSpdD79IHTBN8XnyfjIZLF0KTOzW77ZH+aGXKg8+L9+MxyJOB7Fqdxtju6w6GgfHnPIzFc0DXsT85BFGoKEgT78dvI48fRpStiL3Hs+DzYh7cg2/qZEj9Ko2QRK9WH61VBzBNzFULkCv/CO4QFYPW7TmE3YG8eA7zm0ng9SDqNEG7rR2YJvL4QcxZH4DQ0Lo8gyhQBKSJMeM9OHU0ZNlvVNmb6tN+1HDGNWub01GusXDlWt6bNgtd17m/dTM63NUiqP2t9z9n+96DAJw5f4E80ZHMmPAmsxct58sf56JpGpXjyjDs6cfQtDB+lZ0QRPQdjB5XEen14p7wOvLYkeA+ERFEjngP9/jXMA8fBLsd5/PD0IqVRCYl4p48CnnscPgyX1GxJlqTdmAayI3LkRuWXrebaNACovMiF31vPb6pJaJ2E0i6DIA5dyqcOxm22AhB5ICX0StURno8JI0chnk0sP7sd9yFs8NDYJoYe3eR9PYbICXObo9hb9IMbHZSfpiOZ/YP4YlbvQFa607WmL1yPvKv34M7RMWgPTwgMLZMewe8ntQ340Dv8zrG1xOtMUTT0bqmji02O+ZvM5Fb/g7L+1i0/yRTVu9CF4L2VUvzYLXYoPZjl5N5ecFGDNNEAsOb1SQuf7S/fdjCTeR12nnu5irZmivDgunZZ59FCOF/nJiYiMfjYfTo0dSqVStbg6RL09HaPIQxZSh4U9CfGIaxYz0kXAz0sdnR7n0cUao8ctvq8ORKQ9RujLA7MEY9h4iLR3/gCYwpr/nz6w/2xDeiH6S40V8Yi7FpFaJ6fWTiZczP3oaoGGwvT8a3aRWiTAXM+T9gzv8+9Lnr3Ax2B763+iPKxWPr0BPf5FetRl3H1vFJvG/0hRQ3tiHjMTeshKQEAHxjgk/L6p17Y3z9LvLwPrTb2qLf1RFjxgchy67Va4KwO/AMfxpRvgq2Lr3xjn85kP2hPniG9oIUN45hkzDWr0ArXxV0Hc9rfdGq18P24ON4Jw7D/ujzeKdOQu7eiu2BR9FuboG5fH6Iguto9zyKMX4geFLQn3kLY+tquHwh0KVVB+TaJZirFyFatEfc3Bq54je0Nl0xRvcDr8cqqKrWByFA1zEmDkFUqoXWpivm56NDk/0GtRrYj4bdOpGSmJSjOa7H6/Mx8oMv+HbiW7icTro8N5RmDetRuEA+f58Xez3i79v1+WG81u9J3Cke3vlyBj9PGYPLGcFzI95h8ap1NG9cP2zZbTffjrA7SHr2UbT46kT0fBb3q8/727WKVXA+MwRRqIj/Oftd9yGTk0jq3wNRKhZnnxdIfqlv2DJbwXS0OzpifvYmeFLQHh6M3L0REi8F+tjsiDbdESXjkDvWBZ4vVgbz50/gxKHwZk5lv7U5OCK4/ORD6NVq4uo7kMTBz1iNjghcPftyqVt7SHET9eoo7LfchkxMQK9em8u9uoHTibPzI+EJq+lo9z2O8fZz1tjSfxTGlr+Dx5Y7OyHX/In590LEHfcjbrkTufhnKF0BveNTkK+Qv69ocDskXsaYOh4iY9BfmGC9Xoh5DZORy7Yy88EmuOw2HvpuObeXLUrhKKe/z6SVO+lSsyx3lCvGsoOnGP/XDia2sT6LM7YcZNfZSzQoWTDbs2V4eDRjxgymT5/u/++XX37ho48+YvToMA7IhUsgz54EdxIYBvLgTkRs5eA+Njtyw1LMP38KX640RIVqmFvXAiD370DEVgw0Fi+NPH3MKjQMH3LPVkSFasi1SzF/+jLQL/VCehFbEVGjAfqA0ejd+kOEK2S5tYrVkVvWWLn37UCUrRR4T8XLWLNcV3Lv3oqoVB1RujzCEYHtuRHYBoxGlIsHwPfBW8jD+1JfWAsctYQqe+UaGJusD6/cux0tLk32ErHIk0f92c2dm9Eq10SeOGxlEwJcUWD4rP4FCiN3bwXA3LUFrVKN0AUvWgp55jgkJ1rrdf92RLmqQV1EuSrIHeut97Z9HaJSTfB5Md4ZHFivmg4+j/U70nTrPTld/veUk07v3c8H7R/K6RjXte/QUcqUKEbemGgcdhv1qsezdsv26/b96qdfuaVuTSrHlcFht/HNuNdwOa27hg3DwOGwhzM6erXa+Nb8BYC5Ywt6xeCjZ2F3kPzaQGtmKZVWJg5j9QoA5JGDaGXiwhf4ikLF4Pwpaww3DeTh3VC6YnAfmx25+S/k8rlBT4visWg3t0Hr/gLi5rvCGDo1Vs26eFcuA8DYuglbfJrPqtfD5Se7QYrbeqzbkJ4UbA1vwdi3m6gR7xA9ejLeFX+GJ2yx0sFjy75tiPLVgrqIclWR262CVG5bi6icOvFhs2N8PAJOBmYs5frlmHOmBRY2w3Oz177zCcTmjSKv04FD16hbvABrjwfffPZCk6rcFmsdGBhSEqFbpcyG4+fZeOI8HarHXvO62eEfzyeXKVMmaNYp5JwuSElzpOpxgzMyuI87CblnS/gyXUU4I62N9AppWjtmQDijgtvcydbOOsUNKckQ4UJ/8iWM1OJJHtiJ8d0nGG+/gDxzAu0/XUMX3BmJTEqTzQzkxhmJDMqdhHBFgceN8dssfOOG4Jv6DrYnBlvLXLQ2aFG+KnrzezB+D/EMmSvSf1rwmuxXt7mTEZFRSHcyonAxHKO/wP7Y8/hSM8pTxxDx1sCh1b0ZERE4ksl2zkhrx+HPdp3tOSJNn5RkaxuS0j+rKpq2gQgncudG8CQjChRGHzwZrUNvzKVzQpf9Bq3//mcMrzenY1xXQlIyMVGB9R3lcnH5OjNhHq+PGXPn8+gD7QDQNI1C+fMBMPWneSS5U7ilbs2wZPaLjEImJgQem6ZVLKcytm1Eng4+XWXu3YXesCkAWnx1RMHCgc9JuDhcyJTkwGOPG+G86kDQnQT7t12zqNy2GnPeV5hfjUWUrgAVwrvORdRV69wwQU9d51Iiz58FIOKBLghXJL6//0LLmw9bfDUSX36OpDGvEzVsZHjCOl3B+5qUZGssDOpznbEFYP92uHAmuK8nsI/SHhuEOeer0GVPI8HjI9oROPkV5bCRkBJ8IJjf5cCua+w/n8CY5dvpfVMlTie6effvXQy9LXQHvBmekrsewzC4fPlyKLIE0e54wJpJKloaeWRvoMHhBHdi+gvmAOlOsjbWK4RmDWaAdCdaO8Ar0m7U+QuhPzUUc/Ec5OrFVv/1K/zt5oYV6J2eCl1wdxLC6cJ/tY4Q/txWW9rcVnElTx71X1/FyaPIhEuQtyCcP43W4Da0tp3xvvNy8CnTUEhOCh4MtMA6J/mq34fThUxMwHbXg5ibVuOb+TEUKIzjxXF4hjyK96PR2Lo9Df/phNy3AxmC2THtri6IclWgeCzy0O402a6zPackWTOLXg9EuAKFqxBo7bpD4RKYn42yXve2u5E7NliDWb6C6L1fwxjdH3y5s2DJKRM+n87arTvZtf8gNeMDsxuJycnERF/7vXJ/rd9MgxpVgoor0zQZ88k0Dhw5zsSXnwvvgSNAUiIiMs02L0SmR/3e334mokwcrtEfYGzbiLlnR+BzEmLitnutIqdIKTi2LzDOOJzWmHkD5N/zrZ02IPdsRhQrjdyzKTSBr/fzExMRkWm2D03znw0AQAhcvZ9DKxNLwkvPWstcvIj34H7w+TAPHUCmeBD5CiAvnCMUtLZdrVnqEmWRB3cFGiKuKqDAKpauN7akJ18h9MeHYC6bh1wb2j+L9s7KHaw7do6dZy9Ts2g+//OJHh8xEdeWKquOnOH1P7cw8o7axOWPZurG/Zx3e+j1yyrOJKWQ7DOIyx/NfVVKZ1vGDAumq/8EisfjYeHChbRs2TLbAqTHnD/L+oemoz8zypqV8bgRZeMxl83NeOEwk3u2odVsiLF2KSIuHnl0f6Dx+GFEkRIQGQ0pbrSK1fH98R3E5MPW702M6VOQOzb4u+v93sCcPgV5YBdafG3kwd3X/sBsYu7ZilarEaxZgigXjzx6IPCejh9CFC0JUTHWDE2lGsjfvkVr0hpRKg7jq0mQr4A163TxLFqjFmi3tbGubUoMfUFt7tqCXqcx5qrFiPJVMK+cDgTksYOIYqX82bX4WvjmzkSUjA2cskq8jNBt1nn/2o3wfjgaLpzF1r0v5sbsP09vzvva+oemow+e6N8eRLlqmIuCTyXL/TsQVeoiVy+y/r/POvLWHnzKujD905H+i9JlUkJgp5mUALot/DMI/wL9H+kEWNcl/afn81y4nECk08nqzdt59P521/RfsX4zTevXDnpu2MSPsNvtvDtsQHgv9k5lbNuIrWFTfEvmo8VXxzywJ9NltMpVMbZuIOWDcWgVq6AVLxWGpBb5549WkaTpaE8Ot2Y3PCmIMpWQq37PbHFrZqPnq5jvvwLeFERsPObGZaGOHcS3eT32W27Hu/A39Go1MfYGj8eRL7yC9HpJHNzP/5n0bVpHRIeHSJn+JaJQYYTLhQzhDTD+02aajv7iu4GxpUI1zIXBF5vLfdsRVesh/15o/X/f1vRfOCYfeu/hmLM+QO4KfZHar5F1eYfXMGn39WIuuD1E2m2sOXaOHnXKBfVddeQMI5Zu5YN2N1Eyj3UQ0a1WHN1qWaecf9h+mP3nE7K1WIJMCqbTp08HPY6IiOCJJ54I79cKmAbmvGnoDw8CITDX/QmXz4MrCu3exzG/eSd8WdIhN6xAVqmD/sJYEALj83HWBXNOF3LpPIxZH6H3exMhBOaK3+HCWbQOT0JkNFqbztCmMwDGpKEY0yajd+4NPh9cOo/x1cTQ5V63HKrWxTZkPAiB79OxaA2bQYQLc8lcfDM+wPbsWyA0zGW/woWzmEt/RX90ALbB40BKfJ+NBQl6l6eQZ09j6/2K9dq7NmH8NDVk2c01S9Gq18PxyiQQAu+Ho9Aat0A4XRiLZuOb9h6OQaNBaBh/zoPzZzDmfYu95yD0oe+Absc782NIcSNPHMExcCSkuDG3b8DcuCpkuTENzJ8+Q3/yFWu9rlpgnc6MjEbr2Afzs1GYv3+L1uUZtMYtkQmXMb8aB6XKIRq2gH3b0XtbNxSYS2Yj//wFrfPTaH3fBN1mzTR5UkKX/1/ObrMxqGd3Hn/xTUwpub9VM4oWKsCFywkMHf8+k14ZAMCBI8e4945b/ctt3b2PWb8tol71eB4e9DoA3e+9i5a33BS27L7li9DrNiRy/CeAwD1uOLZmrRHOSLzzrn8Xljx6CPvDvXDc/xAy8TLuca+HLa+faWDOn4nW+VkQArlxmXUhsjMSre3DmN9Nuf5yKcnIRT+gPTQADC/ywA7YG95LL7x/LsDeoDEx708FIUh8cyj2lm0QrkiMHVtx/Kc9vo3riJ74iRX526/wLlmIrXY9Yj7+BoRG0tg3wzOrZxqYP36C/tRw0ATmyvmBsaVzX8xPRmD+PhPtof5oN7dGJl7C/OLtdF9Oa/mAtWzrjtC6IwDG+8NDfn2qXdcY1KQaPX9ehSmhfZXSFI12ccHt4ZWFm5jYpj4jl27Fa5i8OH8DAGXzRzO8WehP1wopM79/+vDhw5w/f56iRYtStGjRG35x38u588LPGyFPn83pCFkiff/eb2E3U/6dp5FshfPldIQse3rCgpyOkCVT9oX29EAoJfR6PKcjZEnkrXVyOkKWXZq7MqcjZElMvRy4SD+biIoVM++UC+l9x6bbluEM05EjR+jfvz92u52CBQty7NgxXC4X48ePp0iRIhktqiiKoiiK8j8jw4Jp5MiRDB48mPr1A981snz5cl577TUmT54c8nCKoiiKoii5QYZXLp47dy6oWAK45ZZbSEhISGcJRVEURVGU/z0ZFkw22/UnoMww3ZaqKIqiKIqSG2R4Su7ChQssWxZ8G6eUkosXQ/wdO4qiKIqiKLlIhgVTtWrVmDPn2m8OLl++fMgCKYqiKIqi5DYZFkzJyclMmDABgE8//ZRHH30UgO7du4c8mKIoiqIoSm6R6UXfVyxevDjUWRRFURRFUXKlDAumtN9peQPfb6koiqIoivI/KcOCKe0flwz7H5pUFEVRFEXJJTK8hmnPnj08//zzSCmD/r13795w5VMURVEURclxGRZMVy74BujUqdN1/60oiqIoivK/LsOC6aabwveXuBVFURRFUXKrDK9hUhRFURRFUTKZYfqvud0hfflQEjFROR0hS4Rh5HSELNM0Vb+H25R9S3I6QpY8Ve7WnI6QZe++9mBOR8gS745/77Wrebq2yekIWeJd8XdOR8iy5Om/53SELMnfN/02tYdSFEVRFEXJhCqYFEVRFEVRMqEKJkVRFEVRlEyogklRFEVRFCUTqmBSFEVRFEXJhCqYFEVRFEVRMqEKJkVRFEVRlEyogklRFEVRFCUTqmBSFEVRFEXJhCqYFEVRFEVRMpFpwXTu3Dn/vxcvXsyKFStCGkhRFEVRFCW3ybBg+uWXX+jYsSNer5fJkyczZcoUpk2bxnvvvReufIqiKIqiKDkuw4Lpu+++46effsJutzN9+nQmTZrEpEmTWLx4cZjiKYqiKIqi5DxbRo26rhMZGcmePXsoUKAARYoUAUL3V+VF1XpoLR8Ew8BcvQi5an5wh8gYtK79EXYH8tI5zBnvgteDuPU/aDe1gMRLABizPoDTx6xlovOg9x+N8cFrgedye/azJ9E69kbkLwI2G+b875Db1oQmd7X6aK06gGlirlqAXPlHcIeoGLRuz1m5L57D/GaSlbtmI7QW7UGC+dfvwe+3TEX0dt0x3h0aksz+7FXrW+vcNDD/XnjtOo9Ku87PY06fDF6Pv1l7oBckJ2DO+cp6veb3oVVrALoNc8VvyL8X5PrcokEztPq3Ww12B5Qoi/HqY+BOCkn2tBauXMt702ah6zr3t25Gh7taBLW/9f7nbN97EIAz5y+QJzqSGRPeZPai5Xz541w0TaNyXBmGPf1YyMaUrCh7U33ajxrOuGZtczrKtSrWQru1HZgmcsMy5Pol1+0mbroDovMiF35nPW7YClGnCSReBsCc+yWcPRm6nEJge7gfWpny4PPi/fht5KnA+KvVaYzt3m5gGBhLfsVYPAe9aWv0pq2tDnYHokwFUvreDzY79kefR0TFgKbh/WBk0GuF2qJ9x5myaie6JmhfLZYHq5cNaj92KYmX56/HME0kMLxFbeLyx7D5xHlGLd0CUlIoysmo1vWIsOnhCS0Etkf6p1n/Y5Anr1r/93W31v+f8zAWz7HWc89BiCLFkcmJ+D5/B3nyaHjyXpU9csDL6BUqIz0ekkYOwzx62N9sv+MunB0eAtPE2LuLpLffAClxdnsMe5NmYLOT8sN0PLN/yPZoGRZMhmGQkJDAr7/+yq233grAiRMn8Pl82R4ETUe7+xGMdwaDJwX96Tcwtq2ByxcCXVo+iFy/FHPNYkSzexGNWiGXzkaULIfxzSQ4uu/a17z/yaCdTUhkc3bRoBkkXraej4xGf3aM9XqhyH3PoxjjB1q5n3kLY+vq4NytOiDXLsFcvQjRoj3i5tbIJXPQ/tMNY9xASHGjD56IsWUVJF5GNL8Xrd7t4HFnf95rsj+CMWFQ6jp/M511vszK3vw+RONWyCWzARCNWiKKl0Hu22Y9Ll8NUTYeY/JLYI9Au/1u5L8gt1y9CGP1Imu59o8j/14YlmLJ6/Mx8oMv+HbiW7icTro8N5RmDetRuEA+f58Xez3i79v1+WG81u9J3Cke3vlyBj9PGYPLGcFzI95h8ap1NG9cP+SZb0Srgf1o2K0TKYmhX4f/mKajteqI+ckb4ElB6zEEuWuD/2ALAJsd8Z+HESXKIXesDTxfvAzmj5/AiYPhiVqvCcLhwPNaX0T5Kti6PIV3QuoBlK5j69obzytPQYobxysTMdavwFj6G8bS36y38fAzyCXzICkRe88XMFbMx/z7T7QqtRHFS4etYPIaJiOXbGFmp9tw2W08NHMJt8cVo3CU099n0srtdKkVxx3lS7Ds4EnGL9/GO21v4pUF65nQ9iZi80Uza8sBjl1OIi5/TFhya/WaIOwOPMOfTl3/vfGOf9lq1HVsD/XBM7SXtf6HTcJYvwL9ptuQ7mS8r/ZBFC+N7eF+eEe/EJa8adlvbQ6OCC4/+RB6tZq4+g4kcfAzVqMjAlfPvlzq1h5S3ES9Ogr7LbchExPQq9fmcq9u4HTi7PxISLJleFjXo0cP7r77bpYsWUKPHj3YtGkTXbp0oU+fPtmfpGgp5JkTkJwIhg+5fwcirkpQFxEXj9y5AQC5Yz2iUg3r+VLl0Frch97ndUTz+/z9tXbdkX/9DpfOZ3/eEGaXG//C/G16YGHTDGHu42lyb0eUqxqcu1wV5I71Vq7t6xCVaoI0MUb2tXbMUTGAgJTUAunMCYzPRoUm7zXZTwRnv2adX5W9Yk2rIbYSIrYSZprZNFG5Nhw/iPbIC2iPDcHctpaQyObcfqXKI4qWvnaGMET2HTpKmRLFyBsTjcNuo171eNZu2X7dvl/99Cu31K1J5bgyOOw2vhn3Gi5nBGAdlDkc9rBkvhGn9+7ng/YP5XSM6ytUHM6dsj53poE8tBvKVAruY7MjN/2FXDYn6GlRPBatSRu0hwcjbmkT8qhapeoYm1YDIPduR4urHMhSItaauUhKAMOHuWsLWuWagfa4Smgly2Isst6DqFgdUaAw9kFj0G5ugbljY8jzX7Hv3GVi80WR1+nAoWvULVGQtcfOBvV5oWl1bitbDADDlEToOgcuJJDP6WDq+r10n7WUi25v2IolAK1yDYxNfwNX1n9gO7lm/e/cjFa5JqJkWcxNq6xljh9GK1EmbHnTstWsi3flMgCMrZuwxafZJ3k9XH6yW2B/o9uQnhRsDW/B2LebqBHvED16Mt4Vf4YkW4YF02233cbChQuZOXMmBQsWpGzZssycOZNmzZplf5IIV/CRcUoyOCOD+zhdkJzkbxep7eaG5ZizPsR4fzgiLh5RpR6i/u3IhEvIXWH4cGVzdjxua4OIcKJ1H4D56zehye2MDM7tdl+bOyJNn5RkhDPK+rdpImo0Qh84DrlvKxgGAHLTSjBCMAN5Tfar17kbXBmtczfCFQkx+dBad8T8/qPgvlExULo85pdjMWd9gN61378jdyqtRXvM378NTebrSEhKJiYqkDvK5eLydWZlPF4fM+bO59EH2lk5NY1C+fMBMPWneSS5U7ilbs1rlssp67//GcPrzekY1xfhRKYkBx573IgIV3AfdxLs23rNonLrasw5UzGnjkGUrggVQ7zOXZGQlBh4bBpw5bTr1W3JSQhXlP+hrV1XfD986X8sChWDxAS8owYiz57C1rZTaLOnkeDxEZ2moI9y2EhICd4+8rsisOsa+89fZszSLfRuVJnzyR42HD9Hp5pxfHLfLaw8fJq/Dp0OW+5r17+Z/vp3JyMio5AH96DVbgyAKF8FChQCEf5T5SIqCpmYEHjCMEFPPZUpJfK8VbBGPNAF4YrE9/dfaHnzYYuvRuLLz5E05nWiho0MSbYMT8l999133H///QDs3r2bihUrAjB58mSefvrpbAmg3dnJOsIuXgZ5aE+gIcIF7sTgzu5kcDohwQMRLmTqTkUunePfCcnt66BkHFqlmiAlVKoJJcqid+5rzXykOfWRW7OzfS3kLYj+yAvWtTTrl2VbZgDtri6IclWgeKx1lHqF03lt7pQk6/14r+QOtMvNKzG2rELr3BfR4HbrdFCIaXd2RsTFQ4lY5ME02SOc1qxNWkHr3IlMTkTUuhkRGYP++EuQJ791rcQp62hLnjpqFXunj4HPC9F5IOES2SFUueXqReCMRBQpibl3S7ZkzciEz6ezdutOdu0/SM34iv7nE5OTiYmOuqb/X+s306BGlaDiyjRNxvxfe/cdHkXVt3H8OzO7m2wKHUILobfQe5cO0ntRiiBiQao0FRBEFERAQEURRAFBARFQQKnSe+i9hBqqEEjfMuf9Y2CTpSQ+ebMbfJ7zuS4usnPObO7ZzJ79zZnZ3bk/cvHqdWaMGoKiKB7P/W+m1G2LElwYgoLh2oXEU8UWX0TCPzt1KPasNw7kAHH2CErOfIizRzySFzAKft8kxZyqJs6Ux8W6HyRY/RCxD18g/fxRcgejnzyU2B79AOdB4+Ns9IO7MHV81XO5H5q+8wRhEX9z+s4DyuTM7FoeY3MQ6PPkjOieK7cZv/kwE5tUpEDmQISIIl+mAApnzQBArZAcnLgVSfV82T2eHXjyMX788U/6t/G1ImKi0Q9sx5Q7H5b3p6GfOYYIPwPCQ2c3kiFiYlD8kowlquo6IAdAUbC+NQQ1XwjR7w821rl/H/ulcHA40C9fRCTYUDJlQUTeJS0lWz6uXLnS9fP48eNdP+/duzfNAuh//IRz1gc4x/ZByZoTrAGgmYxTQRfPuPUVF0+hFK8AgFK8PCL8JPj6oQ2dChbjnLJSuBRcPY/zqzHG/c76ACIuGtcDpWGx5MnsBGRE6zsaffVCxL60L0L0tYtwfjka55hextGb36PcoYiLp91zh59CKfEwd4kKxrUzPla0fh+BZjKKUluC8b8X6H8sNh7zD15FyZYryWNe8umPeYmKSbKfRGxfg/Pz4ThnfYC+6VfEwe2IfZsRF06iFC9vrJghM1h8IOlRznOaG0ApVNKzL35JDHqlCwsmf8D2n2ZzOeIGkVHR2OwO9h09SfkSRZ/ov/PgUWpXKue27IMZ35Jgs/PlB0Ndp+akZxN//Yq+YDL61MGQOQf4+oOqoYQUNcaLlPhYUV//EMzGY60UKI647tlrmfQzx9DKVTV+X6ES6FcSr9EUEZdQgvIYs7qaCbVYGfRzxjV5arGy6MfDHruvo6hlqz5sL4O4etGj2QEG1ijJDx1qs+21F7kcGUNkvA2bU2d/xB3K5cri1nfPldt8suUo37SpQakgo7jKm9GfWLuDS5HGGHIg4m8KZ/XeKTn9zDG0ssk8/jnzJj7+xcuinzuBUrA4+plj2CYMxrl/G+LWda/lTcpx9CDm6rUB0ELL4Dx/1q3db/gY8PEhZuRA16k5x5EwzNVqAaBky45itSIeRKZ5tmRnmESSF8Fn/ZxmdCf6b9+j9R0FioK+dzM8uAvWANROb6L/MBl9wy+oXd5GrdoQEROFvuhzsCWgr1mE9uZYcNgRZ4+6rv/wmjTOrrbuBVZ/1EYdoFEHAJzfTgBHGl+8rjvRV85De30MKCr6no1w/y74BaB27oc+bxL6uqWoLw1Ard4IER2FvnCqkTtsC1r/CeB0IiIuIvZ75pxxstlXfY/Wd7TxmO/b9ORjvn4Zatf+Dx/zB+g/fv7MuxMnD6AUKok2cJJxf8vneOboKo1zA5A9D8KT73h6CrPJxIi+Pejz3gR0IWjfuB5B2bIQGRXN6GlfM3PMUAAuXo2gTcM6rvWOn73Asj83U7FUcXqOMA7CerR5kUY1q3g1/7+S7kRf/zPqy4NBURCHthsHgb7+qC17oi99xufjJcQhNi9H7TEMHA7ExZNw7qhnox7YjlqqIpYxMwGwf/spavX6KL5WnJtX41g0C8vwSaCoOLeuhXt3AB5e0O3+Qm1f9DXmPu9gatAKERuN/asJHs2elFlTGVGnFH1/3YmOoF3JEIICrETG2xiz4SAzWlRl4taj2HWd99YZ1z3mzxzIuAblGN+wPMP/2I8QUC53Fl4okNNrufX92xIff0XBPnsSavUGDx//33H8+BWWEZ8aj/8W4/EXdhumDr0xNetkPM7fTvZa3qTsWzZirlydwK8XgKIQM2E05kbNUKx+OE8dx9KiHY7DYQTMmAtAwtKF2LduwlSuIoFzFoOiEjtlgkeu/VVEMtVPjx49mD9/frI/J8cxtEMaxZT+saRTl/82z9Fby/9XaG979qMfPOXNgnVS7vSc+vLDjukdIVXsZ8LTO0KqmatXTu8IqWLfmXZnc7wtLvxOekdIlcw7nn0wkewMU2RkJNu3b0cI4fbz/fv30zykJEmSJEnS8yrZgik0NJTVq1e7fl60aBGaplGyZMnkVpMkSZIkSfqvkuw5kG7dunHixAk+/PBD6tWrx6FDhzhz5gwNGzb0Vj5JkiRJkqR0l2zBNG3aNCZNmoTZbObzzz/n22+/5ZdffuHbb5/+WTCSJEmSJEn/jVJ8l1zx4sW5efMmcXFxhIaGAsjPTZEkSZIk6X9KsjNM+sO35W3bto3q1Y1PALXZbMTGPoffsyRJkiRJkuQhyc4wVa9enS5dunDjxg1mzZrF5cuXGTt2LM2aef67iCRJkiRJkp4XyRZMffv2pUGDBmTJkoXMmTNz+fJlunbtSqNGjbyVT5IkSZIkKd0lWzABFCpUyPVzvnz5yJcvfb7BWJIkSZIkKb3Ij1aWJEmSJElKgSyYJEmSJEmSUiALJkmSJEmSpBTIgkmSJEmSJCkFsmCSJEmSJElKgSyYJEmSJEmSUqAIIYSn7ty54GNP3bXHibB96R0hVZz3otI7QqqZihVKudNzyHnmQnpHSLWEiHvpHSFV/GqVTe8IqdZvzNL0jpAqs05vSO8Iqeac9Ul6R0iV65tOpneEVAuqHJLeEVLFMufPZ7bJGSZJkiRJkqQUyIJJkiRJkiQpBbJgkiRJkiRJSoEsmCRJkiRJklKQbMF04sSJpy7fsOHfe/GfJEmSJEnSfyrZgmnixImun3v16uX6ef78+Z5LJEmSJEmS9JxJtmBK+okDDofjqcslSZIkSZL+2yVbMCmKkuLPkiRJkiRJ/+1MyTUKIbDb7QghnvhZkiRJkiTpf0WyBdO1a9do2rSpq0Bq0qQJIGeYJEmSJEn635JswbRp0yZv5ZAkSZIkSXpuJXsN0/379/n444/RdZ2zZ8/Svn17unbtSnh4uLfySZIkSZIkpbtkZ5jGjh1L+fLlARg/fjzdunWjaNGifPTRR8ydO9ejwTafucKsbYfRVJV2ZQvTsUJRt/bb0XEMX7EVu1Mne4CVj1vVwmpO3JwPVu8ko9WHIfUrejTnI0poJdTGnUDX0fdsROxe797BPxC1+xAUswVx/y764plgt6GUr4X6QkvQdcT1S+jLvgFVQ+3aHyVrECIhDn3ZbLhz3QOhFUw9BqAEFwKHHft3U+BWhKtZLVcNrVV30J04t/2BvmUNAFrzrqjlq4PJhHPTKvStf0BgJky9hqD4B4CqYp89CW57IPOzFC6DWqu58Tge3oE4vP2p3ZTKDcA/A+KvX8E/A2rrPomNQcGIv35FHNzquZyKgtZ9AEpwQXDYccyb6vaYK2WrobXuBk4n+rY/0LeuBcA0dhbExQAgbt/A+d1nDx/zweAXAKqG41svPuaKgk//kWgFiiDsduI/H4+IuOrex8cHv0++In7ah+hXLoHZjO87H6DmzIOIjSH+i0mIiCveyZtUkbKodR4+5w5tf+bfW6nSEAIyIjb9Ytyu2hilfC2IMb7gWl8zH/6+6bXYKclfpRLtJo1jar3m6R3lCZv2hvHV4hVomkb7RnXo1KSeW3tsfDzjvvqeqzdvY3c4GPV6D8oULcTKTduZ++saAv2stG1Qmw6N63olb6rH8zLVUBu0AwH6rnWIPRsejudvo2TJAZoZff1SxHEPf7m7opD5/Q8wFy2OsNm4N24UjiuXXc3WBo3J0Ps1BIKYZUuI+XWZq03NkoWgxb9w+/XeOC6mw+SIoqC93B8luIAxRv7w+WNjZFW0Fi+D7kTfvg5929rEdQMzYh79Jfap78KNtB9bki2YHjx4QI8ePYiOjub06dO0adMGRVGIi4tL8yBJ2Z06E9fvY0nv5lgtJrp9v5a6RYPJHmB19Zmz8yhtyhSmdZlCfLHlEEvCTtOzaigAPx84zZlbkVQOCfJoThdVQ23dG+e0YWBLQBvwMc7j+yAqMrFL406IA1vR921GadAOpUYTxM4/UZu9jPPTgWC3GU/AkpUgczawxeOcPhKy50Zt/xr6Nx+mfewKNcFswf7RAJRCJTB1eQPHjDFGo6Zh6vomtnH9ICEe8/vT0Q/tQsmVD6VISewTBoLFB+3FTgCYOr+Gvmsj+r4tKMXLoubOh+6tF29VRW3YEf37T8CWgNpjOOLcEYh5kNjHZEZ5sTtK7vyI0weNZTEP0BdNNX7OUxC1TmvEoW0ejao8fMwdEwaiFCyBqcvrOGZ8YDRqGqaub2D/8G1IiMf0/ufoh3ZDbDQAjklD3e5L6/ToMd+KUrwsSq5ghJcec1ONuihmC7GDe6MWL4VP38HEj33H1a4WKYHvgHdRsuVwLTO/2BYRF0vsoF4oeUPw7TecuPf7eyVvYjANtXFn9LkfGftKr3cRZw49ua+06ImSuyDi1IHE5bnyoa+YCzcueTfzP9B42ECqdu9CQkxsekd5gt3hYOKcH1k69UOsPj68NPxD6lUpT/bMmVx95i5fQ5GQvEwa8ganwy9zKvwywUE5mL5wGcunf0QGfz96jZ5ItbKh5A3K7tnAqR3Pt65GbdEd59RhkBCPNnIGzmN7UEIrQ0wUzh+ng18g2tApxv15kLV+QxSLD7d6dMFSuiyZ3hnBnUH9HoZXyThwCDdf6oCIjSXnr6uJ27wBPTISTCYyjx6HSEjwaL7kKOVrgNmM45PBKAWLY+rYF8eXY41GTcPU+Q3sH/U3xsiRU9EP74YH94y27gPB5rns/+irUfbt20elSpVcF3t7umC6cCeSkMyBZLT6YNE0KgTn4MBl9yO5kY0q07J0QXQhuPEghqz+RjF16OotDl+7TafHZqQ8Kigv4s51YwbA6UCEn0QpWNKti1KwBOKU8UItToahFC0DDrtRFNltRidVA4cNJSgYcTLMWHY7AiUor0diK0VKoR81nrji/EnUAomPmZIrH+JWhPFi7XSgnz2GWrQ0aqlKiCvhmPqPwzzoI+MFHVAKh6JkyYZ52Kdo1RugnzzskcxPlTUX3LsN8bGgOxFXzkFwYfc+JjPi2C7EzrVPvQu1URf0PxeBh98BqhYJRTx6zC+cRMn/7MdcnDmGUrQ0Sr5CKBYfTO9MxDT8U5SCJVz3RebsmIZOQq3eAHHqiEezJ6WFlsOxfxcA+qljaEVKuLUrZgtxHw4zZpYeUvMVwLlvJwDi6iXUfAW8ltclWy64eytxX7l8FvI9NlaYzIgjuxDbV7stVnKFoNZqhtpzJErNZl4MnbLb58P5pl239I7xVBeuRJAvVxAZA/yxmE1ULFmUA8dPu/XZHnYUs8nEq2M+5aufV1CrQmmu3LxF8YIhZAoMQFVVShcpyOHT5zwfOLXjudBxTuxv7Fv+gYACCfGIQzvR1y5KXFl3enwTfMpXJG6ncfBnO3oYc2ipJL9f50bb5ojoaNRMmUBR0GONQjvTkOHELP0Z561bHs/4LGrhUMSx/QCIC6dQ8hdxtT0xRp47jlLE2Dat42s4t6xG3P/bc9mSa8yRIwdTp05l5syZtG3blujoaD7//HOKFSvmsUAA0Ql2Anwtrtv+FjPRCTa3Poqi4NQFrb5Zyd5LNyifNwe3o2L5cuthRr9YzaP5nuDrZzxJHomPN5Yl5ZOkT0Iciq+/8eIcfR8ApXYz8PFFnD6MiAg3ZpoAQopCxiygpP3X/ilWP4iNSVyg66A+/D1Wf0TStvhYsPqjBGZELVAUx5cf4vjhc0yvv2vcV7aciJho7JOHI/6+hda8c5rnfSYfX0R8kiLeFo/iY3XvEx8L4Sefvn7hMog7EXDXC6dXrP6IuGc95n7ubfFxKH7+xmzjH0txTBmJ44fpmF4faayTNQhio3F8NsJ4zJt58TH380fERD+2HZrrpvPEYcRt98dTP38GrWptANTipVCyZk/cdm/x8UUk/IN95cLxJ1YVx/ehr16AvmAySnARKFLGw2H/uYPLV+G029M7xlNFx8YR6Jc4HvpbrUTFuB90Rz6I4n50DHM/HE69KhX49LvFhOTOybnLV7lz7z5x8QnsOnyCuHgvzHykdjwH0HWU0tXQhk1FXDgOTifY4iEhHnx8UV8Zhr5mEZ6m+PsjoqISFzidoGlut60NGpFzyQoSDuwDhwO/Vm3R790lfufTL2fwmsfHwaRjpO/Tx0i1RiNE1H3E8QN4UorXMP3yyy8MHDiQF154gUOHDhEdHc3o0aM9Emb65jDCrtzi9K17lMmTOO0aY7MTmKSAesSsqfz+Rht2Xojg3VXbaVQ8hHux8byxeAN3YuKIszspkDUjbcsWfmLdtKC++JJxtJ8rxDhSfcTXF+Jj3DsnxIKP1ZhN8rEm/tEVBbVlD8ieG33eJADEno0oQXnR+o1HhJ+CKxdA6GmeX8TFug8EimLsnGAcXfkmeSHx9YPYaET0A8T1y0Z1f+OqsT2BmYzTWwcfzjgc2o3WPvGrdDxFqdMaJW8hyJEXIsJxzQ1ZHiugUrqfUlUR+7z0jtC4GBRfa2JWt8c8FiXp38PXioiNRty4hrj58Bz+zWuI6AeQKevDx/zhjM2hXajte3tnGwBiY1D8Ht93kj9ytv+5Cp98BbB++g3OE4fRz51K3HYPU+q2RQkuDEHBcO2C+76S8M9OY4k96+FhsSXOHkHJmQ9x1nuzev82ny9YyoETZzhz8QplihZyLY+JiyMwwL0AyZQhgPpVKwBQr0p5vl32GxkD/BnZ52UGfDKDnNkyU7JQCJkzBHosb5qM54A4uhvnsT3GdaiV6yL2boJMWdF6j0Tf/gcizLOn/QFETAyKv3/iAlU1iqYk4jauJ27TBrKM/wT/lm3wa90WBGSvWgNLseJkmTCJOwPeQv/7jsfzugczxsGnjpHxsShur0vGGKk1aANCoJYsjxJcCNOrw3DM/MA4VZeGki2YfHx8eOmll1y3y5UrR7ly5dI0QFID6xlPGLtTp+XXK4iMS8DPYmL/5Zv0qhbq1vfDtbtpUiKEqvlz4e9jRlUUulcpQfcqxqmBXw+fI/zv+x4rloDEaVZVQxs5w7j4NiEepWAo+uaVbn1F+CmUEhUQ+zYb/18wvthY7fgmOOzo301MPB0UXARx4ST6inkQXAg1q2euxRLnjqOWq2Zcd1SoBOJq4gV+4vpllKA8xtRyfBxqsdLY1y5BtdvQGrXD+ccyyJQVxccXoh+gnzmGWrYK+s4NqMVKIyI8f52H2LrSeFKpKuprY42izpaAElzEeHH7h5ScIYhr5z0V041+9jhqueqwb6sxrZ/MY64UK434Yylq7SYoeQvgXDDTeMytfhD5N+LMMdQyVdF3bUApVgZx7aJXtgGMGSRT1do4tm5ALV4K/WLKp0rUYiVxHj9EwjdTUYuUQM3lmVPNTyP++vXhvqKhvjEefI2ZOyWkKGL3nynfgY8V9fUP0WeNAnsCSoHi6IfS+Uj8OTeoe0fAuIapxVsjiYyKxs/Xl33HT9O7nfspzQolirJ1/2FKFS7A/mOnKJwvDw6nk8OnzrNw4vs4nDq9R09kSPdOHsv7/x7Pfaxofd7H+fVYcDqMa2mEgICMaG+MRf9lNuLsUY/lTyrhYBjWF+oRt+4PLKXLYj97xtWm+PuTbcbX3H6jN9jtiLg4hK5zu3d3V5/sc+Zz76MPvF8sAfq5E6hlq8L+rSgFi7uNa+L6ZZQcScbIoqURfy7DcSDxuWga9imOBTPTvFiCFAqm4sWLkzFjRsxm8xNt27d7brAwayojGlWm76L16ELQrlwRgjL4ExmXwJjfdzKjYz26VS7BuDW7mLXtCIoCo1+s6rE8KdKd6Cvnob0+BhQVfc9GuH8X/AJQO/dDnzcJfd1S1JcGoFZvhIiOQl84FfIWRKnaAC6cRHvLuKhb3/o74sIJlGZdUeu1QcTFoP/0hWdiH9iOGloB8/vTQVFwzJ2MWq0++FjRt6zG+dPXmN+ZCKqCc9sfEPk3euTfKMXKYB7zJagK9gUzQeg4fvoac6930Oq1hLgY7F9/7JHMT98QHX3jMtQuAwEFcWQnREeCrx9qsx7oy79+9rrWAGPK3EtE2A4IrYjp/c8BBcfcz1Cr1Xv4mK/BsfhrTO98YlxXsO1P4zHf+gdan2GY3p0GCBzfTQFdx/HzN5h6DUGt3wJiY3B884nXtsOxYzNahar4TZsLKMRPHYepXhMUXz/sa399+rZfu4y55xtY2ndDxEQRP3W81/K66E709T+jvjwYFAVxaLtxMa+vP2rLnuhLv3r6eglxiM3LUXsMA4cDcfEknPPOi9+/ndlkYkSfl+gz5lN0IWjfqA5BWbMQGRXN6JlzmfneQF7v1IrRM+fSeeg4zCaNiYNfx6RpmM0a7QePwWI206vti2TO6LkZJpfUjue2BPSwLWj9J4DTiYi4iNi/BbVNL7D6G++6a2wUfM7Z4xOvXfWAuE3r8a1egxw/LAZF4e6Yd/F7sQWKnx8xvywhds1v5Ji3EBwO7GdOE7t6lcey/KfEwR1QsgKmkdNAAce8qahV6oGvL/rWtTiWfINp0ARQVfTtxhjpLYpI5ntO5s2bx9atWwkODqZVq1ZUqlTpP7pz5wIvvmimMRHm4bd9eojzXlTKnZ5TpmKFUu70HHKeuZDeEVItISLtj8K8wa9W2fSOkGr9xixN7wipMuv0hvSOkGrOWd47mEhL1zc947rLf4GgyiHpHSFVLHOePeOc7AxTr1696NWrFxcuXGDVqlXMnDmT8uXL06pVKwoWLJjmQSVJkiRJkp5H/+gtKgULFmTQoEFMmjSJixcv0rp1a0/nkiRJkiRJem4kO8MEEBkZydq1a1m71vj8mmbNmjF27FhP55IkSZIkSXpuJFsw9e3blxs3btC0aVM++ugjcubM6a1ckiRJkiRJz41kC6Zz54y3Cv/yyy/88ssvbm0bN270XCpJkiRJkqTnSLIFU9Wq6fhWfUmSJEmSpOdEsgXT8ePHiY+Pp2XLlpQvXx6AZD6FQJIkSZIk6b9Ssu+SW7VqFV988QUJCQnMnj2bgwcPki9fPmrXru2tfJIkSZIkSekuxXfJFS1alKFDhwKwb98+pkyZwo0bN1iyZInHw0mSJEmSJD0PUiyYAKKjo1m/fj2///47cXFxtGrVytO5JEmSJEmSnhvJFkxr165l9erVRERE0LhxY8aNG0fevN77wkxJkiRJkqTnQbIF0+DBgylYsCDFixfnzJkzTJs2zdU2ZcoUj4eTJEmSJEl6HiRbMM2fP99bOSRJkiRJkp5byRZMVapU8VYOSZIkSZKk59Y/+vJdSZIkSZKk/2WK8OAnUW4N+vdeIF6jY7n0jpA6fn7pnSDVYg+eT+8IqeJXKl96R0g1JVu29I6QKvZT/859BcBn9MT0jpAqbxZrmN4RUm1m35rpHSFV1Dp10jtCqon9e9M7QqqYpv36zDY5wyRJkiRJkpQCWTBJkiRJkiSlQBZMkiRJkiRJKZAFkyRJkiRJUgpkwSRJkiRJkpQCWTBJkiRJkiSlQBZMkiRJkiRJKZAFkyRJkiRJUgpSVTDFx8endQ5JkiRJkqTnVrIF07Vr1/joo4+YMWMGcXFxAGzZsoWWLVt6JZwkSZIkSdLzINkv333nnXdo27YtERERzJgxA7PZzLp16/jkk0+8lU+SJEmSJCndJVswKYpC586dAahfvz6VK1dm5cqV+Pj4eCWcJEmSJEnS8yDZgslkSmzOlCkTEydORFEUj4eSJEmSJEl6nqQ4w/RIQECA94olRaHwpI8JCC2JnmDjzJBhxF+86GrO8/pr5HypC/a/7wJwdtgIMlSqSFDnTgCovj4EhJZkV+kKOB888FhGtfNbKHkKgMOO88cZcOd6YnOpKqgvdgFdR9+1HrHzz2evk6cAWsc3QOgIhx19/lSIikSp0xy1agMQoP+xGHFsX9pvRomKqA3bGzn3bUbs3ejewS8Q9aUBKGYL4sE99CVfgd0GeQuhtewBKIioSPSfZoLTgdrhDZTsuUDXcS6ZBXdvpnnmZ2+Mgu+AkagFi4LdRtzU8YiIq65mU70m+LR9CaE70cPPEj9jIgjhvXyPYoZWQm3cyXjM92xE7F7v3sE/ELX7EOMxv38XffFMsNtQytdCfaEl6Dri+iX0Zd+AECgN2qGWqgKaCX3HWsSejU//xWmtSBnUWi1BdyIO70Ac2vbUbkrlBhCQEbF5uXG7SiOUcrUgNgoAfc0Cz+4nioKp50DUfIXAYcc+5zPErQhXs1q+OqY23cHpxLn1D5x/rUar3QStdhOjg9mCkq8wCf3bg8mMufc7KP6BoKrYv5nodl+etmlvGF8tXoGmabRvVIdOTeq5tcfGxzPuq++5evM2doeDUa/3oEzRQqzctJ25v64h0M9K2wa16dC4rtcy/xP5q1Si3aRxTK3XPL2jGON0134owQXBbse54HO4nWRsL1MVtflLoDvRd6xDbP8DVA2t52DIGgQmM/qaxYgjeyBXPrRuAwAQV8PRf5oFQvfKZmw+fYVZ2w6hKSrtyhehY4Wibu23o2MZvnwbdqeT7IF+fNy6FlZzYknwwe87yehrYUjDSl7Jm6bjoqqhdu2PkjUIkRCHvmy22+tzaiVbMIWFhVGrVi0AIiMjXT8DbN++/f/9y58l64tNUX18ONS8NYEVK1Bw3GhO9HzV1R5QpjSn+w8i+shR17K48xe4+fNSAAp/8hE3Fv/suWIJUMpUA5MZ55ShkL8YartX0Wd/ZDSqGmr7Pjg/HQy2BLQhn+I8ugelYImnrqN16Itz6ddwLRylZlPURh3Q/1yCWrsZzk8GgNmCNuornMd6pe1GqBpqy544Z74Ltni0t8bjPLEfou8ndmnYAXFwO/qBLSh1W6NUa4TYthqtw+s4F0yBv2+iVKkPmbOh5MgLgPOrMSgFS6K27IH+w+S0zZwMU826YPEhdmAvtBKl8H19MHEfvGM0WnzwfeUtovt2hoR4rO9NwFStNo5dW72WDzAe89a9cU4bZuwbAz7GeXwfREUmdmncCXFgK/q+zSgN2qHUaILY+Sdqs5dxfjoQ7DZj4ChZCeJjUQoUxznjXTD7oNZrjVdKQFVDbdgZfd4EsCWg9hyJOHsYYpI850xmlGY9UPIUQJwKS1yeMx/6qrlw47I3kqJWrIVisWD7sD9KoRKYXnoT++ejjUZNw/TyW9jGvAkJ8VjGzMB5cCfObX/i3PansRk9ByC2roXYGMx9h+PcuQF97xbUEuVQcgV7rWCyOxxMnPMjS6d+iNXHh5eGf0i9KuXJnjmTq8/c5WsoEpKXSUPe4HT4ZU6FXyY4KAfTFy5j+fSPyODvR6/RE6lWNpS8Qdm9kjsljYcNpGr3LiTExKZ3FACUctVRzBack4agFCiO1uE1nLM+NBpVDa1jXxyfDISEeLThU3Ae2YNSqhIiJgp93mfgH4hp1Bc4juxBa9MTfcX3iLPH0HoOQSlbDXFop8e3we7UmbhuL0v6tMBqMdFt3hrqFs1L9gA/V585O47SpmwhWpctzBd/HWTJgdP0rBYKwM8HTnPm5j0qhwR5PCuQ9uNi5mxgi8c5fSRkz43a/jX0bz78/8dMrvHYsWNs376d7du3u/3syWIJIGPVytzb/BcAUQfCCCxb1q09sExpgge8TdlVywke0M+tLaBsGfyKFePGgh89mlEpFIo4+fBF4OJplHxFEhtzBiNuX4e4GHA6EOdPoBQOfeY6znmfwrVwY7mmGTM4MQ9wftIfdCdkyGzcV1rLkQfx942HOZ2Ii6dRCpRw384CxRCnDwEgTh9CKVwasudCxESh1mqO9sZYsAbA7euI4/vQf/nGWDFzdrfCyxu00HI49hmDkfPkMbSiJRMb7TZiBvaChIcfiaGZEDabV/MBEJQXcSfJvhF+EqVgSbcuSsESiFMHARAnw1CKljFmJKePNPYNAFUDhw2leHmIuITaayRqn/fQT+z3znZkywn3bkF8rDHDdOUsBBdx72MyI47uQuxY47ZYyRWCWqMZao/hKDVe9HhUtWgpnEeM2Vlx/iRqgWKJWXKHIG5eg9hocDrQzxxDLVYmsb1AUdQ8+XFuXm3cLlIKJUt2zCMmo9ZogH7qsMfzP3LhSgT5cgWRMcAfi9lExZJFOXD8tFuf7WFHMZtMvDrmU776eQW1KpTmys1bFC8YQqbAAFRVpXSRghw+fc5ruVNy+3w437Trlt4xXJTCoejHDwAgwk+hhCTZr3MFI25HuPYXce44SuFQxIFt6CvnJ/ZzOo3/vp6AOHsMNBNkzAwP7nllGy7ciSQkSyAZrT5YNI0KwUEcuHzLrc/IxlVoWaYQuhDceBBLVn8rAIeu3OLw1dt0qlj0aXftGWk9LgYFJ77W3o5ACcqbJjFT/Bymv/76i+HDh/Paa68xevRodu/enSa/ODlaYCCOB1Gu28LpNAqJh26tWMXZ4SM50r4zGapUIUujBq62fAP7c2nKNI9nxNfqXsToTlAfPpy+fu5tCXHg6//sdR49iQoUR63TAn3zioftOkqdFmhDP0M/uMMz2xCf5KguIQ6sfu59fPwS+yTEofj6gV8GlPzF0Hf9iXP2eJTCpVAKl3JlVjv1Q23dC3HE8/tKUop/AMREJy7QdeMJBCAEItI4hWtu3RnF14rzgHfzAca+kfQxj483liX1xGPub5w6fFiAKrWbgY8v4vRh8M8A+Qqj/zAZfenXaN0Ge2c7LFZEQlzibVs8iq/VvU98LISfeGJVcWIf+tqF6AunoAQXhsJlnuiTpqx+EPuM5+rjbXGxKFZ/101Ty5dx/Jr4Qqhkywkx0dgnDUP8fQtT8y6ezZ5EdGwcgX6J+4q/1UpUTJxbn8gHUdyPjmHuh8OpV6UCn363mJDcOTl3+Sp37t0nLj6BXYdPEBef4LXcKTm4fBVOuz29Y7goj4/fQnftL4qvv3tbfBxY/Y0DsYQ48LGivf4+zkfFk9AhSw5MH3wNARkQN6/iDdEJdgJ8LK7b/hYz0fHuB4iKouDUBa1mrWDvxeuUD87B7ahYvtxyiNHNqnklp0saj4siItyYaQIIKQoZs4Dy//+c7mRPyf34449s3bqVHj16kDVrViIiIvj666+5dOmS691znuCMikILSBy0FFV1VewA12bPwRllFFR3N2wkoFQp7q7fiJYhA9bChbi/w/NTnsQbT44kIY0XaDD+qEn/2D4PC6Vk1lEq1EZt0gnnrLEQnXhaQ2z9HeeOP1DfGgdFSiPOJp6GTC21SWeU/MUhVwji8tkncyaVEGssd9jBx4qIjzGuPblzA25dMzKeOQx5CsK5YwDoS76ENRnR+n+M87MhYPfO4Cxioo3B6xFFMV4ck9z2eW0gat58xH443CuZHlFffMk4Jfv4Y+7rC/HPeMztNuMxf/Q3URTUlj0ge270eZOMZbFRiFtXwemA2xHGOgEZPTa7p7zQxihycuSFiAuJp/8svoj4f3ZKRezdYLy4AOLcUZScwYhzRzySF4C4WOPg4BE1yXM1Ltb9IMHqh4h9WHT7+aPkDkY/eSixPfoBzoPG+KIf3IWpY+KlAp7y+YKlHDhxhjMXr1CmaCHX8pi4OAID3F9UMmUIoH7VCgDUq1Keb5f9RsYAf0b2eZkBn8wgZ7bMlCwUQuYMgR7P/W8l4h/bX5KM0yI+xnjhfiTpQXDmbGhvjkb/azVi31+Jfe7ewjGmD0rNJmgd++L8forHsk/fFEbYlZucvnmPMnkST7nG2OwE+lqe6G/WVH5/qy07L0Tw7optNCoRwr24BN5YtJ470XHE2Z0UyJaRtuWKPLFuWvDUuCj2bEQJyovWbzwi/BRcuZAm144lW3L99ttvfPXVV9SsWZPixYtTv359Zs+ezW+//fb//sXJebB3P1ka1AcgsGIFYk6ecrVpgYFU2rIR9eGRVqZaNYl6eC1TxupVidzm2dOFj4gLJ1BCH1aw+YshIi4mNt64gpI9N/gFgGZCKVwKEX7qmesoleui1mmBc/q78PfDi19z5EHt857xs9MBDjsijS5Q1v/8Gec343B++JpxxGz1B01DKVACcemM+3ZePG2c9gGUYuWMne/uTfDxNS5wBKP4unkFpUJtlHptjBXtNqP699IFjgDO44cxVa0JgFaiFHq4+2kH30Hvo1gsxnVNj07NeYm+dhHOL0fjHNPLeMwf7RsFQxEX3U+riPBTKCWMFz2lRAXEBWOWRu34Jpgs6N9NdE1BiwsnXX8fMmQGiy/EROEpYssK9IWfoX/+DmTOYRwYqBpKvqJw7ULKd+BjRe07FszGR5MoIcUR1y95LC+AfuYYWrmqxu8rVAL9SmJOEXEJJSgP+AeCZkItVgb93MPHu1hZ9ONhj93XUdSyVR+2l0FcvejR7ACDundkwSfvs33BF1y+fpPIqGhsdgf7jp+mfPHCbn0rlCjK1v3GacL9x05ROF8eHE4nh0+dZ+HE95k4+A3Cr16nQgkvnm75lxHnTqCWqgyAUqA44tHlEgDXr6DkSBzb1SKlEBdOQmAmTAMnoC+fh9i5ztVde+sDyJHbuJEQ5/HxcGD9CvzQ80W2vdOFy/ceEBmXgM3pZP/lm5TL637N2odrdrEn3LgQ2t9iRlUUulctybLXWvJDzxfpU7M0LUoV8FixBJ4bFwkugrhwEueXo9GP7jYuPUkDyc4wmc1mtCSnwgAsFssTy9LanTVryfRCbcr+vgJFUTg9cAjZ27VB8/fnxoIfCf94EmWXL0G32YjctoN7GzcB4FeoEPGXPDv4PiIO70IpXh5tyGRQFJwLP0ep9IIxJbjjT/Tlc9D6fQiKir57Pdz/+6nroKioHV6He7fRXnvfuO+zR9HXLEJcC0d75zMA9OP7XTM4aUZ3ov82H63P+0bOfZuN04NWf9QOb6AvmIK+cTlq536oVRsYFzUumgFOJ/rSWWhdB4IC4tIZ49yy2Qe101uob4w13rG16ntjZspLHDs2Y6pYFb/PvwNFIf6zcZjqNUWxWnGeOYm5aWucxw7iN/lrAGy//oRjx2av5QOMx3zlPLTXxxiP+Z6NcP8u+AWgdu6HPm8S+rqlqC8NQK3eCBEdhb5wKuQtiFK1AVw4ifaWcfGivvV3xNE9KIVKog3+1Li/X2Z7p0jVnegblqB2HQyKgji83bhA09cPtXlP9F9mPX29hDjE5l9Ruw0Fpx1x8RScT+P9+vGoB7ajlqqIZcxMAOzffopavb5xWnbzahyLZmEZPgkUFefWtXDvDsDDC7rd31ljX/Q15j7vYGrQChEbjf2rCR7NnpTZZGJEn5foM+ZTdCFo36gOQVmzEBkVzeiZc5n53kBe79SK0TPn0nnoOMwmjYmDX8ekaZjNGu0Hj8FiNtOr7YtkzihnmJ5FHNqJKFEebfgUY5z+fipK5brga0VsW4tz2bdoAyegKAr6znUQ+Tdqp9eN53CzrtCsKwDOmaPR/1iC1nOIcdBrS8A5/3OvbINZUxnRqAp9f1yHLqBducIEZfAnMi6BMb/tYEan+nSrUoJxq3cxa+thFEXx/mm4pNJ6XLxwAqVZV9R6bRBxMeg/fZEmMRWRzLRFjx49mD9//j9e/ritaXShVXqo0bFcekdIHT+/lPs8p2IPnk/vCKniVypfekdINSVbtvSOkCr2U//OfQXAZ/TE9I6QKm8Wa5jeEVJtZt+a6R0hVdQ6ddI7QqqJ/XvTO0KqmKb9+uy25FY8fvw4Xbq4X9QohOD8+X/vYCVJkiRJkvSfSrZgWrlyJdu3b6datWqYzWauX7/OmTNnqPMvrnolSZIkSZL+U8le9L1ixQp27txJUFAQefLkIWfOnOzcuZOVK1d6K58kSZIkSVK6S7Zg2rJlC9OnT8dqNd5imTdvXqZNm8amTZu8Ek6SJEmSJOl5kGzBZLVan/j+OLPZjL+//zPWkCRJkiRJ+u+TYsF05coVt2VXrlzx3pfwSpIkSZIkPQeSveh76NChvPXWW1SvXp3g4GAiIiLYvn07kyZN8lY+SZIkSZKkdJfsDFORIkVYtGgRJUuWJC4ujtDQUBYvXkzJkiWTW02SJEmSJOm/SrIzTACBgYG0adPGC1EkSZIkSZKeT///r++VJEmSJEn6LycLJkmSJEmSpBTIgkmSJEmSJCkFsmCSJEmSJElKgSyYJEmSJEmSUqAIIYSn7twxvJOn7trj7Bevp3eE/zn7toSnd4RUqdYyNL0jpFrMyYj0jpAqGV5ult4RUk2cPZPeEVJFxMand4RU6z97R3pHSJUvp7yS3hFSTXtjfHpHSB2/jM9skjNMkiRJkiRJKZAFkyRJkiRJUgpkwSRJkiRJkpQCWTBJkiRJkiSlQBZMkiRJkiRJKZAFkyRJkiRJUgpkwSRJkiRJkpQCWTBJkiRJkiSlQBZMkiRJkiRJKUi2YBo+fDj79+/3VhZJkiRJkqTnUrIFU+PGjZkzZw6tWrXihx9+4P79+97KJUmSJEmS9NwwJdfYsGFDGjZsyJ07d1ixYgWvvPIKhQsXpnPnzlSqVMlbGSVJkiRJktLVP7qGKVu2bPTp04effvqJ3Llz06tXL0/nkiRJkiRJem4kO8P0yP79+1m5ciUHDhygYcOGrF692iNhlBIVURu2B11H37cZsXejewe/QNSXBqCYLYgH99CXfAV2G0rt5qiV60PMAwCcy2ej5CuKWqmusZ7JDLnz4xzfF+JjPZI9cSMUzH2GoIYURtjt2L+ehLh5zb2PxQfLqGnYv56IiLgMmob5zXdRsudEMZux/zIf/YCXv13735r7YfbCkz4mILQkeoKNM0OGEX/xoqs5z+uvkfOlLtj/vgvA2WEjyFCpIkGdOwGg+voQEFqSXaUr4HzwwONZtZf7owQXAIcdxw+fw62IxOayVdFavAy6E337OvRtaxPXDcyIefSX2Ke+CzeuoAQXROvaD4QT7HYc302GB5GezZ9kO/yGjkIrXAxhsxE78QP0a1dczeaGL+LbqRvoOs7zZ4j97CMQAt/ur2KuVQ9MZhJ+/Qnb7796J28Smy9cZ9ae02iqQrvQEDqWyu/WHvEgllEbDuLUdQQwrkE5CmQO5OiNe0zadgyEIJu/L5OaVMTHpHk8rxJaCbVxJ2Nc3LMRsXu9ewf/QNTuQ4xx8f5d9MUzjXGxTDXUBu1AgL5rHWLPBlA11K5vo2TJAZoZff1SxPF9HgitoHbthxJcEOx2nAs+h9vXE5vLVEVt/pKxn+9Yh9j+B6gaWs/BkDUITGb0NYsRR/ZArnxo3QYAIK6Go/80C4Se9plTIX+VSrSbNI6p9Zqnd5QnFSyFWq0J6Dri+G7E0V3u7YGZURu/BKoKioK+/ie4d8toM5lR2/dDX7cocZkXbdqyjS9nz8GkabRv04pO7dq4tV+5do2Ro8chEOTOlYvxo97DavVlxe9rmDt/IYEB/rRt2YKObVunaa5kC6YZM2bw+++/kz9/fjp27MgHH3yAyfSPaqz/nKqhtuyJc+a7YItHe2s8zhP7ITrxuim1YQfEwe3oB7ag1G2NUq0RYttqlDwFcf78BVwLd/UVt6/jPLDFWK/Nq4j9mz1fLAFq5dpg9iFh1JsoRUpi7tEP2+T3XO1KwWJYXhuKkjW7a5lWuwlE3cf2xUcQkAGfT78jwcuFx781N0DWF5ui+vhwqHlrAitWoOC40Zzo+aqrPaBMaU73H0T0kaOuZXHnL3Dz56UAFP7kI24s/tnzxRKglK8BZjOOTwajFCyOqWNfHF+ONRo1DVPnN7B/1B8S4jGNnIp+eDc8uGe0dR8ItgTXfWld3sS5+EvElQuodZqhNe2Ec8lsj28DgLlOfbD4EPV6N7TQMlj7DyNmpPGihsUHa9/+POjeDhLi8R87CXPNFxAx0WilyhH1Rnfw9cW36yteyZqU3akzcesxlnR5AavZRLclW6lbICfZ/X1dfWbuPslLZQvQsFButl+6ybQdJ5jevApjNh7k8+ZVCMkUwLJjF4mIiqVA5kDPBlY11Na9cU4bBrYEtAEf4zy+D6IiE7s07oQ4sBV932aUBu1QajRBbF2N2qI7zqnDICEebeQMnMf2oIRWhpgonD9OB79AtKFTjPtLY0q56ihmC85JQ1AKFEfr8BrOWR+6tknr2BfHJwONbMOn4DyyB6VUJURMFPq8z8A/ENOoL3Ac2YPWpif6iu8RZ4+h9RyCUrYa4tDONM/8n2o8bCBVu3chIcbzryv/MVVFrdsW/cfPwG5D7TIIcf4YxEa5uig1mqEf2grnj0JIcdRaLdF/mwtBwagNOkNgpnSJbrc7+GTKNJYt/B6r1UrXV/pQr04tsmfL5uozedpMunRsR8sXm7J0+QrmLfyRLh3aM/3Lr/n1pwVkCAzklTf6Ub1qZfLmzp1m2VI8JffDDz8we/ZsGjVq5LliCSBHHsTfNyAuBpxOxMXTKAVKuHVRChRDnD4EgDh9CKVwaWN5ngKo9dqivfkhSr027vebtyBKUF7EnsdmqzxEK14G/dAeI+PZE6iFiru1K2YLts/eR7922bXMuWsz9p/nJHZyOr2SNal/a26AjFUrc2/zXwBEHQgjsGxZt/bAMqUJHvA2ZVctJ3hAP7e2gLJl8CtWjBsLfvRKVrVwKOKY8c5TceEUSv4irjYlVz7ErQiIjQanA3HuOEqRUgBoHV/DuWU14v7frv6O2Z8grlwwbmga2O1e2QYAU5kK2HdvB8B5/Aim4iUTG+02ol7vDgnxD7OZELYETFVr4rxwFv9PphPw6RfYd27xWt5HLtyNIiSTPxl9LVg0lQq5s3Ig4m+3PsNrl+KF/DkBcOoCH03jYmQ0mXwtLDh4nh7LtnE/3u75YgkgKC/izvWH46IDEX4SpWBJty5KwRKIUwcBECfDUIqWAaHjnNjfOEj0DwQUSIhHHNqJvnZR4sq6Z56zSuFQ9OMHjEzhp1BCEvdzcgUjbj+2nxcORRzYhr5yfmK/h+OJ8+sJiLPHQDNBxszGAcRz4Pb5cL5p1y29YzxdlpwQeQcS4kB3Iq5dgDyF3LqILSsg/LhxQ1URzofjh2ZCXzUH7t70buaHzoeHky84LxkzZMBiNlOxfFn2Hzzk1ufchXDq1KwBQIVyZTlw6DBXr12jeLGiZMqYEVVVKR1aksNHjqVptmQroBw5crB169antnXu3DlNg+BrdZ8BSogDq597Hx+/xD4JcSi+Rrt+eCdi55+QEIvaYxiUqIA4GQaAWq8t+oZlaZs1OVZ/RGy066bQdVA118Cknz765DoJccb/vlYsQ8bj+OlbbyR192/NDWiBgTgeJB45CafTKCAeDri3VqwiYt73OKOiKTlvDlkaneLueqOAzjewP5emTPNeWKsfIi4m8bauG1Piug6+j7XFx6H4+aPUaISIuo84fgCaJXne3TdOMSqFSqLVb4V90lAvbQQo/v6ImMT9Baee+JgLgbhnFCE+HV5Csfrh2LsLS73GqDlzEz2sH2ruvARMmsGDrq28lhkg2uYgwGJ23fa3mIhOcC80M1t9AAi/F8XkbceY2bIq9+JsHLp+l/frliEkUwBvrdpNyRyZqJ4vOx7l6+c+LsbHG8uSemJc9Dd+1nWU0tVQO7yGOHHA+Ns4Hm6rjy/qK8PQ1yzCE5TH92WRuJ8rvv5GAejapjiw+icW2D5WtNffx/moeBI6ZMmBadDHiPgYxM2rHsn8nzq4fBVZQ/Kld4yns/giHo3PAPYEFB8rImmf+Id/g8w5UOu0MYokgIhw0lN0TAyBAQGu2/5+/kRHRbv1KVGsCJv+2krbVi3YuGUrcXFxhOQL5tyFC9z5+2/8/fzZtWcf+fOl7d8n2YLpzp07afrLnkZt0hklf3HIFYK4fDaxwcfq/qQCSIg1ljvs4GNFPPyDi+2rjScdIE6FQe4CcDIMfP1QcuRBP3/c49vhEheDkqTQUxTlHx3FKVlzYBk6Ace6X3Hu2ODJhE/3b80NOKOi0AL8EzOpqtts17XZc3BGGQXV3Q0bCShVirvrN6JlyIC1cCHu7/Di9H5crPFi4gqrGMUSQHwsiq81sa+vFREbjdagDQiBWrI8SnAhTK8OwzHzA3hwD7XyC6jNu2CfPtrt9LWniZgYFL/Ex5zHHnMUBetbQ1DzhRD9/mBjnfv3sV8KB4cD/fJFRIINJVMWRORdj+edvvMEYRF/c/rOA8rkzOxaHmNzEOhjfqL/niu3Gb/5MBObVKRA5kCEiCJfpgAKZ80AQK2QHJy4Femxgkl98SWUgiWeHBd9fRNf6B55NC7abca4mGTcFEd34zy2B7Vrf5TKdRF7N0GmrGi9R6Jv/wMRts0j+UV8rHEQ/IiiuvZzER9jFHmubUoy1mfOhvbmaPS/ViP2/ZXY5+4tHGP6oNRsgtaxL87vp3gk97+dUqM5Sp6CkD03XL+UOM6YfdwLqEeCi6DW74j+x4J0uVYpqWlfziLs4GFOnz1HmVKhruUxsTEEBrrP5o4YMojxEyfz+5/rqF6lMpkzZSJjhgy8+85g+g8dSc4cOQgtUZzMmTKlacZkC6bSpUvzwgsvpOkvfJz+58/GD6qGNnSqcaRhi0cpUAJ9yyq3vuLiaZTi5REHtqAUK4cIPwW+VrQhU3B+NhhsCSiFShnXK/FwqvrsU2ZGPMh5+ihaxZo4d21GKVIS/fKFlFfKmBnL+1Owf/c5+rEDng/5FP/W3AAP9u4nS+OG3Fn1O4EVKxBz8pSrTQsMpNKWjeyrVRc9NpZMtWpyY7Gxz2WsXpXIbdu9mlU/dwK1bFXYvxWlYHHEtYuuNnH9MkqOPMYplPg4lKKlEX8uw3EgMaNp2Kc4Fsw0iqVq9VHrNMcxeTjERD3lt3mO4+hBzDXrYt/0J1poGZznz7q1+w0fg7DbiRk5EIQxbDuOhOHTqRsJP81HyZYdxWpFeOki9YE1jNNYdqdOywUbiYy34Wc2sT/iDr0qFnbru+fKbT7ZcpRv2tQgTwbjhT1vRn9i7Q4uRUYTkimAAxF/0z40xGN5XafNVA1t5AzwC4CEeJSCoeibV7r1FeGnUEpUQOzbbPx/4YQxS9PnfZxfjwWnw7j2TQgIyIj2xlj0X2Z7dGwU506glqmK88A2lALFEUmuL+X6FZQcuV3bpBYphWP9LxCYCdPACTh/moU4dcjVXXvrA5zLvjXeHJEQ99xc8P08EjtXG0WSqqL2fM+YjbQloOQtjDiwyb1zcBHUuu3Ql8+CqPQ/zTm435uAcQ1T8/adibx/Hz8/P/aHHeLVHu6nPnfu3kO/1/tQvGgRvpv/IzWqVcXhcHD46FF+nPsNDqeTXq/3Y/Dbb6VpxmQLprlz53q8YHLRnei/zUfr8z4oKvq+zca5aqs/aoc30BdMQd+4HLVzP9SqDYyLAxfNAHsC+h+L0V7/ABwOxLmjrvP5ZM+N8PJ5WH3vVrQylbCM/wpFUbB99QlazYbga8W58benrmNu2x0lIBBT+57QvicAto+HGkeMMneK7qxZS6YXalP29xUoisLpgUPI3q4Nmr8/Nxb8SPjHkyi7fAm6zUbkth3c22gMHH6FChF/6ZJXs4qDO6BkBUwjp4ECjnlTUavUA19f9K1rcSz5BtOgCaCq6Nv/hMi/n35HiorW9S3E37cwvTXauO/TR3GuWuCV7bBv2Yi5cnUCv14AikLMhNGYGzVDsfrhPHUcS4t2OA6HETBjLgAJSxdi37oJU7mKBM5ZDIpK7JQJibNrXmLWVEbUKUXfX3eiI2hXMoSgACuR8TbGbDjIjBZVmbj1KHZd5711xkFA/syBjGtQjvENyzP8j/0IAeVyZ+GFAjk9H1h3oq+ch/b6GGNc3LPROBXrF4DauR/6vEno65aivjQAtXojRHQU+sKpYEtAD9uC1n+CcU1oxEXE/i2obXoZY2rjTtDYeJeoc/b4NH/OikM7ESXKow2fAoqC8/upKJXrGrOm29biXPYt2sAJKIqCvnMdRP6N2ul1Y7uadYVmXY1sM0ej/7EErecQV+HnnP95mmb9r6Tr6FtWoLZ7ExQVcWy3MQPt64faqCv6b3NR67YDzYTa1ChGxL1biA0/p3NwMJtNjHxnEK++NQAhBO1btyQoRw4i799n1IcT+GLKpxTIH8J7Y8djsVgoUqggY0YOx2QyYTabafdSD3wsFnp1f5ksmTOlaTZFCCGe1di9e3e+++47ntbFYrGkeOeO4Z3+f+nSkf3i9ZQ7SWlq35b0PXeeWtVahqbc6TkVczIi5U7PoQwvN0vvCKkmzp5J7wipImLj0ztCqvWfnQ4fd5IGvpzySnpHSDXtjfHpHSF1/DI+synZGabDhw/TtGlThBDGNS3g+nnjRu+860ySJEmSJCm9JVswlS1blgULvDPFL0mSJEmS9Lz6R1+N8oj88l1JkiRJkv4XJTvDNHq0cTHp3r17+fDDD3E6nTRt2pTcuXPTsWNHrwSUJEmSJElKb8nOMBUtWhSA6dOns3DhQrJly8Ybb7zB4sWLvRJOkiRJkiTpefCPTsmpqkqmTJlQFAUfHx/8/f1TXkmSJEmSJOm/xD8qmPLly8eUKVOIjIxk9uzZ5E7DL7OTJEmSJEl63v2jgmncuHHkzp2bihUrYrVaGT/+X/r5CpIkSZIkSamQ7EXfrk4mE127dvV0FkmSJEmSpOfSf/SxApIkSZIkSf+LZMEkSZIkSZKUAlkwSZIkSZIkpUAWTJIkSZIkSSmQBZMkSZIkSVIKFCGE8NSdO78c5qm79rw7d9I7QaoIhyO9I6SaEhSU3hFSp1Sl9E6QamL5ovSOkCqOu1HpHSHVbh+9nt4RUiX38J7pHSH1bv47H/N+73yf3hFS7dMGhdM7Qqpk2BD2zDY5wyRJkiRJkpQCWTBJkiRJkiSlQBZMkiRJkiRJKZAFkyRJkiRJUgpkwSRJkiRJkpSCZAumy5cveyuHJEmSJEnScyvZgmnAgAG88sorrFmzBse/+O3qkiRJkiRJ/x/JFkwrVqxg2LBh7N+/n5YtWzJ58mQuXbrkrWySJEmSJEnPBVNKHUJDQwkNDcVms7FhwwYmTZpEQkICc+fO9UY+SZIkSZKkdPePL/q+d+8eV69e5c6dO2TLls2TmSRJkiRJkp4ryc4wxcXF8eeff/Lrr7/y4MEDOnTowJw5c8iQIYO38kmSJEmSJKW7ZAumhg0bUr9+fd555x3KlCnjrUySJEmSJEnPlWQLpnXr1uHv7++6ff36dRwOB8HBwR4PJkmSJEmS9LxItmA6c+YMY8aMIU+ePLRo0YKJEyditVrp1KkTr732mkeDbb5wg1l7z6CpCu1K5qNjqRC39oioWEZtOIRTFwgB4xqUpUDmAI7evMekbcdBQDY/HyY1qYCPSfNo1icULYtapzXoTsShbYiwrU/tplRtBAEZERuXGQtKVESt2RwQiANbEAefvp4nKcXKo9ZtA7oTPWwr4sBfT+9XvQlKQEb09Utcy9QXX0bcuY7Yt8k7YZPYHP5of1FpVyL4GfvLYZxCIIRgXH1jf/n+4Hl+OXGZLFYfAMbWK0OBzAHey334NLNW/2XkrlmejrUrubVHxsTSbPRMiuTJAUDDcsXp3qA6q/ceZf7GXWiqStG8QYzp2hxV9fzn0CqlKqM26WLsH7s3IHatc+/gH4jacyiK2YK4fxf9x+lgtxltZgtav/E4F82AW9dA1VBfHoCSJQeYzOh/LkEc2+vhDVAwvTIINV8hcNixz5mMuBnhalbLV8fUtgc4nTi3rMX512owmTH3HYGSIxciLgbH99MRN695Nuczsmd+/wPMRYsjbDbujRuF40riZ+VZGzQmQ+/XEAhili0h5tdliduVJQtBi3/h9uu9cVwM93r0zaevMGvbITRFpV35InSsUNSt/XZ0LMOXb8PudJI90I+PW9fCak58efrg951k9LUwpGGlx+/a8wqWQq3WBHQdcXw34ugu9/bAzKiNXwJVBUVBX/8T3LtltJnMqO37oa9blLjsOZG/SiXaTRrH1HrN0zuKO0XBd8C7qIWKgt1G3JTxiIgrrmZTvSb4tHsJoevoF84SP+MTEAIArXgpfF4bQOw7fT0SLdmC6eOPP2bmzJncv3+fV155hQ0bNhAYGEj37t09WjDZnToTtx1jSec6WM0mui3dTt0CQWT393X1mbnrFC+VKUDDQrnYfukW03aeYHqzyozZeJjPm1UiJFMAy45dIiIqzqsvgKgaapOu6N9+CLYE1N7vI04fgpgHiX1MZpSWvVDyFESc3G8sUxTUBh3Rvx0HtnjUtyYgToVBXLR3s7/4Ms6vx4A9Aa3PGJynD0L0fbfsaptXUfIWQhzfZyzzC0Rt/zpKtpyI7de9l/chY385zpJOtY39ZdlT9pfdp3mpTP4k+8tJZjSvzInb95nYqDyhOTKlQ24nE5f+wZJ3+2L1MdPt07nULVOM7BkDXX1OXL5Os8qlGNU1cVCLt9mZsXIjKz54C6vFwtA5S/nr6Bnqly3u2cCqhtq2D87PhoAtAW3QJJzH9kJUZGKXpl0Q+7eg792E0rA9Ss2miL9WQXBhtM5vQqbEN4woletCTBTOBdPALxBt+OfG/XlyEyrWQjFbsI17G6VQCUwvvYV92iijUdMwdeuHbfQbkBCP5YOZOA/uRKvyAiI+DvvYfii5gjH1HIj90+Eezfk01voNUSw+3OrRBUvpsmR6ZwR3BvV7uGEqGQcO4eZLHRCxseT8dTVxmzegR0aCyUTm0eMQCQlezwwPn5/r9rKkTwusFhPd5q2hbtG8ZA/wc/WZs+MobcoWonXZwnzx10GWHDhNz2qhAPx84DRnbt6jckiQ98OrKmrdtug/fgZ2G2qXQYjzxyA2ytVFqdEM/dBWOH8UQoqj1mqJ/ttcCApGbdAZAjN5P3cKGg8bSNXuXUiIiU3vKE8w1awHFguxA15BK1Ea3zcGEzdmiNFo8cG311tEv9YZEuKxvvcxpmq1cezaiqVTT8yNmiHi4z2WLdlDUl9fX/Lnz0/ZsmUpUaIEWbNmxWKx4Ovrm9xq/28X7kURktGfjL4WLJpKhdxZOBBx163P8NqhvJDfeAI5dYGPpnExMoZMvhYWHLpAj2U7uJ9g826xBJAtF9y9BfGxxgzTlTMQ4n40hcmMOLwDse23xGVCoH/5HiTEgTUAFAVsnvvDP1X23Ii7N43sTifi8hmUkGJPZj+4HX3LqsRlFl/0zb8iDu3wbt6HLtyLTnl/qVXSfX95OOt44tZ9vt1/jm7LtjN7/1nv5r5+m5DsWcjob8ViMlGhcD4OnHP/dP0TlyI4eeU6PT77jkHf/Mzt+1FYTBo/juiD1WIBwOHU8TGn+Akh/385gxF3rkNcDDgdiAsnUAqFunVRCpZEnAwDQJw4gFKsrNFgMuOc8wncvOrqKw7uQF/9Y+LKutPjm6AWK43ziFGUifMnUQskPjeV3CHGzFFsNDgd6KePohYrg5InP/qRPcY616+g5s7n8ZxP41O+InE7twFgO3oYc2ipxEZd50bb5ojoaNRMmYyZjljjxTDTkOHELP0Z5630meG4cCeSkCyBZLT6YNE0KgQHceCye5aRjavQskwhdCG48SCWrP5WAA5ducXhq7fpVLHo0+7a87LkhMg7xrisOxHXLkCeQm5dxJYVEH7cuKGqCKfd+Fkzoa+aA3dvejfzP3D7fDjftOuW3jGeSitVDse+nQA4Tx5FK1oysdFuI2ZAL0h4+NqoaQibMYOtX79C3NihHs2WbMGkKIrrZ5MpcUAWD6e/PCXa5iDAx+y67W8xEZ1gd+uT2eqDWVMJvxfN5O3HeatqMe7FJXDo+l26lC7A3LbV2X3lDruu3PZo1if4WBHxcYm3E+JRfPzc+8THwoXjT64rdCheEfWNDxGXznjlBcSNj9XI9khCHPha3fvExxpHWElF3oar5z2f7xmibXYCLEn2F7OJaFsy+8uOE7xVxRiAXyySmw/qlea7tjUIi7jLX+HeG9yi4xMIeHgqEMDf14foOPciuUDO7PRrWY/5Q3vToFwJJvy0BlVVyZbBOBBYuGk3sQk2apRwH8Q9wtdqFEuPJMSB9bF929cvcR9KiEPxfXgNZPhJ44UnKVu8cR8+VtRXR6CvXui57I9Y/SA2yTbounEq5Wlt8XEofv6IS+dQy1UHQClUArJkA8X7X8Op+PsjohJnNnA6QdPcblsbNCLnkhUkHNgHDgd+rdqi37tL/M7tXs/7SHSCnQAfi+u2v8VMdLzNrY+iKDh1QatZK9h78Trlg3NwOyqWL7ccYnSzat6OnMjii0hIMp7bE1B8Hh8TY4z9KHMO1DptELv+MJZHhEN0pNei/icOLl+F025PuWM6UPz8ISbJmRXdCerD/VwIRKRxMGxu0xnF6ofzwG4AHNs2ITz8jSTJHpYeP36cLl26IITg3Llzrp/Pn/fMi+P0XScJi7jL6TsPKJMzs2t5jM1BYJIC6pE9V+4w/q8jTGxcgQKZAxBCkC+TP4WzGqc0aoXk4MStSKoHZ/dI3qSUeu1Q8hWBoLxw9QKuktLHFxH/H0x7njqAfioMpc2rKGVrIg55fqBTG3RACSkKQcGIpIXP4wXUc2b6rlOEXX+4vwRlci2PsT9jf7l6h/F/HWVio/Ku/aVHuYKuvi/kD+Lk7fvULeDZqf/pKzYSdv4yp6/epEyBPIm54xMItLrP3lYrXgDfh8Vgw/LF+WKVcX2Yrut8tnw9l27+zfQ3Orsd3KQ1tfnLKAVLQu78RiH/iM9jBRQY+4uP1bhuyceKeLz9cZmyofV5F337WsQBL1yzFxfrXuSpqvFi96gt6QGCrxURE41+YDum3PmwvD8N/cwxRPgZ4+DGy0RMDEqSN+GgqkbRlETcxvXEbdpAlvGf4N+yDX6t24KA7FVrYClWnCwTJnFnwFvofz9WvHrA9E1hhF25yemb9yiTJ3EMjrHZCfS1PNHfrKn8/lZbdl6I4N0V22hUIoR7cQm8sWg9d6LjiLM7KZAtI23LFfF4dqVGc5Q8BSF7brh+KXE8N/u4F1CPBBdBrd8R/Y8Fz921Sv82IjYG/JLs54rqPnmgKPi8NhA1bwix44Z5NVuyBdOqVauSa05zA6uXAIxz3i0XbiYy3oaf2cT+a3/Tq4L7EfSeK3f4ZOtRvmldjTwZjAEwb0Z/Yu1OLkVGE5IpgAMRf9O+ZMgTv8cTxOblxpNK1VDfmgC+/mCLR8lXDLHzj5TvwOKL2nUg+sIp4HSAPcF1IZun6Y8uOlc1tAETwfowe0gx9O1rvJIhNQZWN67ZsTt1Wv74V5L95S69yj+2v1y9wydbj/FNq6qu/SXa5qD1or/47eV6+Jk19ly9Q9uSnn8H6MA2DR7mdtJy7BdExsTi52Nh/9lL9GpU063v6PkraVShJC9WKsXuk+GUDMkNwNgff8NiMjHzzS4ev9jbddpM1dDe+xL8AoyZ08Kh6Jt+desrLpxEKVkRsXeT8f/TZlIfCcyE9tY49GXfIM4c8eAWJNLPHEMrXx19z18ohUqgX7ngahMRl1By5gX/QIiPQy1eFseaJSgFi6OfOYbjx69QChRFyZHbK1kfl3AwDOsL9Yhb9weW0mWxn00sXhV/f7LN+Jrbb/QGux0RF4fQdW737u7qk33OfO599IFXiiWAgfUrAA+fn7N+JTIuAT+Lif2Xb9Kruvup3A/X7KJJifxULZALf4sZVVHoXrUk3asap2N+PXSW8Dv3vVIsAYidqx+O5ypqz/eMmVNbAkrewogDj72pJbgIat126MtnQdQ9r+T7b+Y8fghTtTo4tqxHK1EaPfycW7vv4PfBZifugyFee418JNmC6e2336ZOnTrUrl2b8uXLo2neebeZWVMZUTuUvit2owtBu5L5CAqwEhlvY8zGQ8xoXoWJ245h1wXvrT8IQP7MAYyrX5bxDcoy/M8whIByuTLzgodnC56gO9HXLUbt9g4oCuLQNuOiWF9/1Fa90Jd88fT1bPGIo7tRXxlpnCu/eRVxZKdXo6M70dcuQusx3LgGImyrMQBY/VHbvIq+eIZ38/xDxv5Skr4rd6MLaFcyOMn+cpgZzSszcetx7E6d9zYcAiB/Jn/G1S/LoOrF6fXrTiyaStW82V3XOXknt8aIDk3pO32BsZ/XKE9Q5gxExsQyZv4qZrzZhSHtGjHqhxX8tGUfVouZ8T1ac+JyBL/sOEjFwvnoNe0HALrXr0bD8iU8G1h3oq+Yi/bmOFAV9N0b4P5d8AtA7doffe4n6OuWoHYbhFqjCSLmAfoPnz3z7tRGHYx1m3SGJp0BcH49LvFddZ7YhP3bUEtVxDJmJigK9tmTUKs3QPG14tz8O44fv8Iy4lNQVJxb1sK9Owi7DVOH3piadULERmP/drLH8iUnbtN6fKvXIMcPi0FRuDvmXfxebIHi50fML0uIXfMbOeYtBIcD+5nTxK727gHvs5g1lRGNqtD3x3XG87NcYYIy+BMZl8CY33Ywo1N9ulUpwbjVu5i19TCKoqTvabikdB19ywrUdm+CoiKO7TbeBOPrh9qoK/pvc1HrtgPNhNrUuCZI3LuF2PBzOgf/93Js34ypQjX8ps8DRSF+8lhM9Zsap99On8DctA3Oowfx++wbAGzLF+PYsdkr2RSRzAVJ165dY8+ePezdu5fjx4+TP39+ateuTe3atcmVK1eKd+780rvTZWnqjneOwtKap8/hepISlA7vgkkLpdLhrc5pRCxflN4RUsVxNyrlTs+p20e9/07StJB7eM/0jpB6N/+dj3m/d75P7wip9mmDwukdIVUybAh7ZluyM0x58uShXbt2tGvXDiEEmzdvZs6cOYwbN47jx5OZapckSZIkSfovkmzBdPfuXbZu3cpff/3FqVOnKFeuHC+//DJfffWVt/JJkiRJkiSlu2QLptq1a9OkSRP69OlDqVKlkusqSZIkSZL0XyvZt9dMmjQJk8nEqFGjGDVqFOvXryc62oufPC1JkiRJkvQcSHaGqUWLFrRo0QIhBEePHmXr1q18//33aJrG/PnzvZVRkiRJkiQpXaX4fQqRkZEcOHCA/fv3c+jQISwWC5UrV/ZGNkmSJEmSpOdCijNMQgiqV69OzZo16d+/P35+fsmtIkmSJEmS9F8n2YLp22+/JVeuXPz66698+umn2GyJHyi3ceNGj4eTJEmSJEl6HiRbMD36cMo5c+bw9ddf/6MPq5QkSZIkSfpvk+I1TADBwcGEhHjnO9kkSZIkSZKeN/+oYPL19aVPnz6UKFHC9a3oQ4YM8WgwSZIkSZKk58U/KpheeOEFT+eQJEmSJEl6bv2jgqlt27aeziFJkiRJkvTcSvaTviVJkiRJkiRZMEmSJEmSJKVIEUIIT925rU8TT921x2l55UcoeJvS5N956ldf+kN6R0g1pUCB9I6QKg9+WpfeEVLNv0Tu9I6QKmrgv/dDi00Tvk/vCKnyoFW99I6QasM3nkvvCKnytXjwzDY5wyRJkiRJkpQCWTBJkiRJkiSlQBZMkiRJkiRJKZAFkyRJkiRJUgpkwSRJkiRJkpQCWTBJkiRJkiSlQBZMkiRJkiRJKZAFkyRJkiRJUgpkwSRJkiRJkpSCZxZMAwYMcP28ZcsWr4SRJEmSJEl6Hj2zYLp3757r57lz53oljCRJkiRJ0vPoH52S8+DXzUmSJEmSJD33TMk12u12V7GU9GeLxZL2SRQF7eX+KMEFwGHH8cPncCsisblsVbQWL4PuRN++Dn3b2sR1AzNiHv0l9qnvwo0rkCsfph4DQVEQVy7gXPQVCD3tMz9L0XKoL7QCXUcc3IYIe/opTaVaYwjIiNiw1LhdqqqxTOiIm1cRq+eDN4vVf2tuYPPBE3y1agOaqtKudmU61a3q1h4ZHcuLIz+lSJ6cADSsWIoejWtx9MIVJv30G0JAtoyBfNq3Cz4Ws0ezKiUroTbuZOzLezcidm9w7+AfiNptMIrZgrh/D/2nmWC3oZSphlq/HSDQd61H7DHW04Z8BvGxAIi7t9B/+sKj+R/ZHH6TWfvOoCkK7UoG0zE0xK09IiqOURsP49R1BDCuXhkKZA5wtX+w6QgZfc0MqVHCK3kBUBT8ho5CK1wMYbMRO/ED9GtXXM3mhi/i26kb6DrO82eI/ewjEALf7q9irlUPTGYSfv0J2++/ei9zkuxpNkZ6I27oo/1cR9+zEbF7vXsH/0DU7kMe7ud30Rc/3M/L10J9oaUxDl2/hL7sG1A11K79UbIGIRLi0JfNhjvXvbIdm7Zs48vZczBpGu3btKJTuzZu7VeuXWPk6HEIBLlz5WL8qPewWn1Z8fsa5s5fSGCAP21btqBj29ZeyQuAouA74F3UQkXBbiNuynhEROLf3VSvCT7tXkLoOvqFs8TP+MQ1ZmvFS+Hz2gBi3+nrvbz/gfxVKtFu0jim1mvu9d/9zILp2rVrNG3aFDBmmJo0aQKAoihs3LgxzYMo5WuA2Yzjk8EoBYtj6tgXx5djjUZNw9T5Dewf9YeEeEwjp6If3g0P7hlt3QeCLSFxo9r1wrl8HuLsMbRe76CUq4Y4uDPNMz+VqqE27Yo+exzYE1B7v484cwii7yf2MZlRWvVCyVMQcfJA4rL67dFnjTIGjfZvQNGycPqQzJ0Cu8PJxMW/seSD/lh9LLw84SvqlStJ9kyBrj4nLl2jedVyjOrexrVMCMGYecv4/O3uhARlY+mWPUT8fY8CuXJ4LqyqobbphXPacLAloPX/GOfx/RAVmdilcSdE2Db0fZtR6rdFqd4YsW0NavNuxnoJ8WgjpuM8tgcS4gFwfjXGc5mfwu7Umbj9OEs61sJqNtHtlx3UzR9Edn9fV5+Zu0/zUpn8NCyYk+2XbjFt1ylmNKsEwM/HLnHm7wdUzpPVq7nNdeqDxYeo17uhhZbB2n8YMSMfXq9p8cHatz8PureDhHj8x07CXPMFREw0WqlyRL3RHXx98e36ilczP5KWY6THqRpq6944pw0z9vMBH+M8vu/J/fzAVmM/b9AOpUYTxM4/UZu9jPPTgWC3GQVVyUqQORvY4nFOHwnZc6O2fw39mw89vhl2u4NPpkxj2cLvsVqtdH2lD/Xq1CJ7tmyuPpOnzaRLx3a0fLEpS5evYN7CH+nSoT3Tv/yaX39aQIbAQF55ox/Vq1Ymb+7cHs8MYKpZDywWYge8glaiNL5vDCZuzBCj0eKDb6+3iH6tMyTEY33vY0zVauPYtRVLp56YGzVDxMd7Jed/qvGwgVTt3oWEmNh0+f3PPCW3adMmNm7cyMaNG9m0aZPrnyeKJQC1cCji2H4AxIVTKPmLuNqUXPkQtyIgNhqcDsS54yhFSgGgdXwN55bViPt/u/o7vhqPOHsMNBNKxizwINIjmZ8qey64e8s44nc6EZfPQr6i7n1MZsThHYhtvycuczrQ534EdhsAiqqBwy5z/wMXrt8iX46sZPT3w2IyUaFIfg6cCXfrc/ziVU5cukb3T2Yx6IsF3Ip8wMUbt8kU4M/8ddvp/sks7sfEebZYAgjKi7hzA+JijH05/CRKQfcZFqVACcSpgwCIUwdRipYFoeOcNMD4+/gHAopRLOXODxYf1NfHoL45DkKKPvk7PeDCvWhCMvqT0deCRVOpkCsLB67fdeszvFZJXggxHk+nEPhoxnBz6Po9Dt+4R6dSIU/cr6eZylTAvnu7ken4EUzFSyY22m1Evd7dVYSimRC2BExVa+K8cBb/T6YT8OkX2Hemz5tg0nKM9LigvIg71x/bz0u6dVEKJtnPT4ahFC0DDrtRFD0cT1A1cNhQgoIRJ8OMZbcjUILyemUzzoeHky84LxkzZMBiNlOxfFn2Hzzk1ufchXDq1KwBQIVyZTlw6DBXr12jeLGiZMqYEVVVKR1aksNHjnklM4BWqhyOfcYkgfPkUbSi7vt5zIBeSfZzDWEzHm/9+hXixg71Ws7/1O3z4XzTrlu6/f5nFkw2m40ffvgBIQQ3b95kwIABDB06lNu3b3smidUPEReTeFvXQX0Yz/extvg4FD9/1BqNEFH3EccPuN+X0CFLDswfzoaADAgvTUED4GNFxCepfm3xKL5W9z7xsXD+uPsyISDmAQBKlYZg8Xmyjyf9W3MD0XHxBPglzmz4+/oQFRfn1qdgrhy83bYxC959kwYVQpmwcCX3omM5eO4iXetX57thfdl94hy7Tpz1bFhfK8QleZwT4sDX/8k+j/4W8XEovn7Gz7qOUroq2tCpiAsnwOkEewL6XyvRv/kQfdnXaC8PSnzeeFC0zUGAJXGC2t9iIjrB4dYns9WCWVMJvxfN5B0neatKUW7HxPPl3jOMfqG0xzM+jeLvj4iJTlzg1EHTjJ+FQNwzigqfDi+hWP1w7N2FmjETpuKhxIwaQuzk8fh/MDEdkpO2Y6Sn+fol7sMA8fHGsqR8kvRJiEPx9TfGk4ez2krtZuDjizh9GBERbsw0gXFQkDELKF7Yz2NiCAxIPI3s7+dPdFS0W58SxYqw6a+tAGzcspW4uDhC8gVz7sIF7vz9N3Fx8ezas4/Yx8YkT1L8/CHpfq47jeITjP080ji4MbfpjGL1w3lgNwCObZsQDsfjd/fcOLh8FU67dw/Ik3rmKbnx48fj5+eHruuMHTuW0qVLU6RIEcaOHcuXX36Z9kniYlF8/XBd+aIoxoAAEB/r/uLta0XERqM1aANCoJYsjxJcCNOrw3DM/MCYhr57C/v7vVFrN0Xr/DrO7z5L+8xJKPXboeQrCkF54eqFxO2w+LoXIsneiYLSqBNK1pzoS7xzHcq/NTfA57/8QdiZi5y5ep0yBfO5lsfEJ5DBz73Yq1aiEL4+xrV3DSuWYuav68jk70e+oGwUzhMEQK3SRTl+8RrVSxYhrakvdkUpUAJyhyAuJSnKfKzGUXhS8XHGcrvN2NeTtIuje3Ae24vapT9KpbqIsK3GjBXA7esQGwUZMkOkZ2YTpu8+RVjEXU7/HUWZoEyu5TE2B4E+Tw4ne67eYfyWY0xsWI4CmQNYcDice/E23vhtD3diE4hzOCmQOYC2JYI9kvdxIibGeDF5RFWNwvMRRcH61hDUfCFEvz/YWOf+feyXwsHhQL98EZFgQ8mUxfWi4zVpPUZ6gPriS8aMaa4QY5balccX4h/bzxNiE/dznyT7uaKgtuwB2XOjz5sEgNizESUoL1q/8YjwU3DlgkevS5325SzCDh7m9NlzlCkV6loeExtDYGCgW98RQwYxfuJkfv9zHdWrVCZzpkxkzJCBd98ZTP+hI8mZIwehJYqTOVMmj+V9nIiNgaT7uaIaRZPrtoLPawNR84YQO26Y13L92z2zYIqIiGDu3LkkJCRw4MABZsyYgdls5rvvvvNIEP3cCdSyVWH/VpSCxRHXLrraxPXLKDnyGKci4uNQipZG/LkMx4HtiRsy7FMcC2bCg3uY3h6LY8ls44LI+DivXIAsNi03BjJVQ+03Aaz+xixNSDHEzrUprQ6A0uIVcNrRf5rhtYum/625AQa1N66xszuctHj/MyKjY/HztbD/dDi9X3zBre+oectoXKk0L1Ypy+4T5wjNn5e8ObIQG5/ApZt3CAnKxoEzF2lfu7JHsuprFxs/qBraiOngFwAJ8SgFS6L/tdKtrwg/hVKiAmLfZpTi5RHhJ8HHitbnPZxfjwOnA2zxIHSUqg1QcoWg/zLbKJR8rB57MQQYWK04YFzD1HLRX0TG2/Azm9gfcZde5Qu69d1z9Q6fbDvONy2rkCeDMbvQvWwBupctAMCvJ68Qfi/aa8USgOPoQcw162Lf9CdaaBmc591nFP2Gj0HY7cSMHOjalx1HwvDp1I2En+ajZMuOYrUivHma/6G0HCM9lnHtIuMHVUMbOSPJfh6KvjmZ/bxEBWPWFFA7vgkOO/p3ExPHk+AiiAsn0VfMg+BCqFmDPLYNAIP7vQkY1zA1b9+ZyPv38fPzY3/YIV7t4X5KaOfuPfR7vQ/Fixbhu/k/UqNaVRwOB4ePHuXHud/gcDrp9Xo/Br/9lkczJ+U8fghTtTo4tqxHK1EaPfycW7vv4PfBZifugyFef4POv9kzCyZFUQAICwujdOnSmM3GO4cSEjxz4aA4uANKVsA0choo4Jg3FbVKPfD1Rd+6FseSbzANmgCqir79z2SPoJ1rl2DqPRQcxguL44fPPZL5qXQn+p8/oXZ7BxQVcXCbcaGj1R+1VS/0n58xA5MrBKVCbbh0BqXnCOOudq+DU2EydwrMJo2RXVry2pQ56LqgXe3KBGXOSGR0LKPnLWNm/x6807EZ789dwuKNu7D6WBjfuwMWk4mPendk2NeLEQjKFw6hbjkPv2NLd6Kv/B6t7xhQFPS9G+H+XfALQO30Fvr3n6KvX4r60gDUao0QMQ/QF04DWwL6ga1ob39kXGN2/RLiwFZQVZSub6O9PQEQOH/+MnHWwYPMmsqIWqH0XbUHXUC7EsEEBViJjLcxZtMRZjSrxMRtx7E7dd7bcAiA/JkDGFevjMezJce+ZSPmytUJ/HoBKAoxE0ZjbtTMOC1x6jiWFu1wHA4jYIbx2XMJSxdi37oJU7mKBM5ZDIpK7JQJXnmMH5eWY6TH6U70lfPQXh8Dioq+J8l+3rkf+rxJ6Ose7ufVGyGio9AXToW8BVGqNoALJ9HeMi7q1rf+jrhwAqVZV9R6bRBxMV57J6jZbGLkO4N49a0BCCFo37olQTlyEHn/PqM+nMAXUz6lQP4Q3hs7HovFQpFCBRkzcjgmkwmz2Uy7l3rgY7HQq/vLZMmcySuZARzbN2OqUA2/6fNAUYifPBZT/abGfn76BOambXAePYjfZ98AYFu+GMeOzV7L92+liGd8yNKAAQOoWbMmf/75Jy1atKBNmzb88ssvbNmyhS+++Gc7q61PkzQN601a3lzpHeF/jtKkbXpHSBV96Q/pHSHVlAIF0jtCqjz4aV16R0g1/xLeeadUWlMD/VLu9JwyTfg+vSOkyoNW9dI7QqoN33gu5U7Poa/Fg2e2PfOqubFjx3L58mUaNGhAu3bt2LNnD+vXr6dMmfQ9QpQkSZIkSfK2Z56Sy5IlC8OGGReDHTlyhF9//ZXjx4+TN6933s4pSZIkSZL0vHhmwWSz2Vi9ejU//vgjFouF6OhoNm7ciK+v77NWkSRJkiRJ+q/0zFNy9evX5/Tp03z22WcsWrSIHDlyyGJJkiRJkqT/Sc+cYerRowe///47165do0OHDvILeCVJkiRJ+p/1zBmmvn37smrVKrp3787vv//OsWPHmDx5MmfOnPFmPkmSJEmSpHSX4mfLV6lShcmTJ7N+/Xpy5szJ8OHDvZFLkiRJkiTpufGPv4wnQ4YMdO/enRUrVngwjiRJkiRJ0vPH899eKEmSJEmS9C8nCyZJkiRJkqQUyIJJkiRJkiQpBbJgkiRJkiRJSoEsmCRJkiRJklIgCyZJkiRJkqQUyIJJkiRJkiQpBYqQ33kiSZIkSZKULDnDJEmSJEmSlAJZMEmSJEmSJKVAFkySJEmSJEkpkAWTJEmSJElSCmTBJEmSJEmSlAJZMEmSJEmSJKXAlN4BHrly5QqTJ0/mxo0b+Pr64uvry7BhwyhSpEh6R/vHXn75Zd5++22qV6/uWvbRRx/x22+/sW3bNiwWyxPrLF++nIwZM9KgQQMWLlxIt27d0iTLnj176NGjB9OmTaNZs2au5S1btiQ0NJSJEydSv359cuXKhaqqOJ1OYmNjGT9+PKVLl3a7r1KlSlG+fHkA4uPjqVWrFv3790dVn15vz5w5k2zZstG1a9c02ZZ/4p9s78CBA5k4cSKVK1d2bQ9AoUKFGDt2rNeyPsvs2bOZP38+GzduxMfHJ73juNmzZw+DBg2icOHCrmWZM2fGz8+P48ePkylTJhwOB5kzZ+bdd98lODj4qftBp06dmDp1Knnz5mX//v18+eWXOBwOYmNjadeuHS+//LLHt2X27Nns3LkTVVVRFIXBgwezcOFC13Y80qpVKzp27MiWLVv47rvvXM+TDh060KpVK49mTGl/3rt3LwULFmTOnDmutnnz5jFx4kROnz5NfHw8Y8eO5datWyiKQkBAAGPHjiVz5sxuz/tHRowYQalSpTyyLWfPnmXy5MnExcURGxvLCy+8QNu2bWndujWhoaEIIbDZbLRq1co1/iUdc+x2O7quM2XKFIKDgz2S8Z84ffo0H330EQCHDh2iTJkyqKrKq6++ytGjR8mWLRu3bt0CYODAga711q9fz59//slnn33mtawRERG89tprrF69GoDff/+d4cOHs23bNrJmzcrVq1d5++23+eKLL2jVqpXr7xAXF8d7771HsWLFaNy4MevXr8ff3991v61bt2b69Onkz5/f49vw+Hh49+5dPvjgA2JjYxFCkDt3bkaNGoWvr+8T+3TGjBn54osv0j6UeA7ExsaK5s2bi7CwMNeyw4cPi27duqVjqv/cihUrxIgRI1y3ExISRP369UVMTMw/Wr9GjRpplmX37t2iadOm4s0333QtO3XqlGjQoIErY7169UR8fLyrfevWraJv377J5tJ1XYwePVrMnz//mb97xowZYtGiRWmxGf9YStsbHx8vBgwYIIRI28c5LbVo0UJMmDBB/PLLL+kd5Qm7d+8WgwYNemL5iBEjxJYtW1y39+3bJ9q1ayeEePp+0LFjR3HlyhVx+fJl0bp1a3H79m0hhBBxcXGiY8eObvflCWfPnhWdO3cWuq4LIYQ4ceKEaNmy5RPbkVTdunXF/fv3hRBCREVFifr164s7d+54NGdK+3O9evVEixYtxN9//+1q79mzp6hcubIQQoiFCxeKyZMnu9rmzZsnxo8fL4R48nnvSffv3xctWrQQ4eHhQgghHA6H6Nevn1i0aJHo2LGjq5/NZhOvvfaa2LhxoxDiyefo4sWLxbhx47yS+Z94/DF8tK9fu3ZNNGzY0LV/CSHE66+/Lvbu3ev1jE2bNnXtH0OHDhUDBw4Uy5cvF0IIsWzZMvHZZ5+JK1euuP0dLly4IJo3by6EEOK9995zG4uOHj0qunfv7rX8j4+HkyZNchtPPvroIzFv3jwhhPf26efilNzmzZupVq2a21F/mTJlmD9/PiNHjuSNN96gS5cu3L9/n4kTJ9KxY0c6duzIDz/8AMDIkSPZunUrAFu3bmXkyJEANGjQgCFDhtChQwfeffdddF336HY0bdqUPXv2EBcXB8DGjRupWbMmLVq0ICEhgXXr1tGxY0e6du3K0KFD0XWdmTNnsnjxYmbNmsX9+/fTdKajePHiXL9+nQcPHgCwatUqWrZs+cz+ERERZMiQIdn7VBSFXr16sWbNGgDWrl1L586d6dq16xNHUE6nk/fff59XX32Vdu3a8fnnn6PrOo0aNSIyMhKARYsWuR0l/38kt727du2iatWqafJ7PGHPnj3ky5ePLl268OOPPwJw5MgR2rdvT48ePRg8eLBrv16wYAGdO3emS5cuzJ8/Pz1jP6FSpUqYzWYuXbqUbL+VK1fSpk0bsmXLBoCvry9z586lZs2aHs2XJUsWIiIiWLZsGTdv3qREiRIsW7Ys2XWyZs3K/PnzOXv2LP7+/qxdu5asWbN6NCek/Pxt0qQJf/zxBwDnz58nX758mM1mAPLkycOOHTvYtGkT0dHRdO/e3bX/eNPGjRupWrWqa0ZC0zQmTZpEtWrV3PqZzWZ69OjhGlce90/GprRmt9t57733ePnll+natSt79uxJcZ3cuXMTEhLC/v37Abh9+zbXrl2jcuXKHs26fPlyBg4cyOuvv86LL77I8uXLqVGjBmFhYei6zpkzZ+jduzd//fUXAHv37qV27dpP3M+DBw/IkycPYMwGr1ixwtX2yy+/0LlzZ49uxyNPGw/z5MnDn3/+yc6dO4mPj2fEiBF0797dK3keeS4KpqtXr5IvXz7X7TfffJPu3bvTtGlTbty4QbVq1fjpp58ICwvj6tWrLFmyhEWLFvH7779z+vTpZ97vzZs3GThwIMuWLSM2NpYNGzZ4dDt8fHxo0KAB69evB4ydOOkO9vvvv/PKK6+wePFiatWqRXR0tKvtzTffJGPGjGl+aqhRo0asX78eIQRHjhxxK0oBevfuTYcOHahTpw5HjhxhxIgRKd5ntmzZuHfvHpGRkcycOZPvv/+exYsXc/PmTXbs2OHqd/36dcqVK8fcuXNZvHgxixcvRlVVWrZs6ZoqXrVqFW3atPH49v7111/UrVsXgPv379O9e3fXv2PHjqXZ70+tpUuX0rFjRwoWLIjFYuHw4cN88MEHTJw4kfnz57ueH+fOnWPNmjUsWrSIRYsWsWHDBi5cuOCVjLt373Z73J5V6GbNmpV79+49834UReHWrVvkzZvXbXlgYCCapqVp5sdlyZKFWbNmERYWRufOnWnatCmbN28GYPLkyW7b92hsmTVrFnFxcQwZMoRatWrxzTffILz0BQnJPX9btGjB2rVrgSeLqbp16/Lmm2+ybNkyGjRowCuvvML58+dd7b1793ZtZ8+ePT2W/9atW0+cRvP393cVdkk9Glcg8Tnatm1b6tWrR0JCAq+99prHcj7N0qVLyZw5Mz/++CNfffUVH3744T9ar1OnTqxcuRKAFStW0L59e0/GdImOjuabb75h1qxZzJ49mxo1arB//36OHTtGaGgopUuX5tSpU+i6zokTJ1z70rlz5+jevTtdu3alZ8+eNG/eHICyZcty//59rl+/js1mY+fOnTRq1Mgr2/K08bBr1660aNGCuXPnUrt2bd5++23XKVBw36cfFYZp7bm4hilnzpxuL1qzZs0CjB0vZ86cFChQADCOoipVqoSiKJjNZsqWLes2CABuA1muXLkICQkBoHz58oSHh3t6U+jYsSOffvopVatW5cGDB4SGhrra3n33Xb755hsWL15MwYIFadiwocfztGzZkrFjxxIcHEylSpWeaP/uu+/w8fFh6tSpXL169R8dOV+7do2cOXNy+fJl7t69S9++fQGIiYnhypUrrn6ZMmXi6NGj7N69m4CAAGw2GwAdOnRg8ODBVK5cmWzZsrlmGdLCs7b3xo0b5M6dGzDOby9YsCDNfuf/1/3799m6dSt3795lwYIFREdHs3DhQm7duuW6hq9ixYqsWbOGM2fOEBERwSuvvOJa9/LlyxQsWNDjOatVq8a0adPclj1t1iIiIoKcOXPi4+Pj+ps/Ehsbi6+vL7lz5+bGjRtubadOnUIIQYkSJdI+/EOXLl0iICCATz75BICjR4/St29fypYty7Bhw6hTp45b//v37xMREcGwYcMYNmwYN2/epH///oSGhlK/fn2P5Xwkuedvrly5AOPAJCwsjEGDBrnaDh48SPXq1WncuDFOp5OVK1fy7rvvsnz5ciDxee9puXPn5sSJE27Lrly58sTfHhLHFUh8jjqdTkaOHInZbHa7lsYbzpw5w4EDBzhy5AgADoeDe/fukTlz5mTXq1evHlOnTiU+Pp7Vq1czb948b8SlePHigLFf2Gw2qlatyrfffktAQAAvvPACiqJQtmxZNm/e7DYbWbhwYdd4ePv2bdq2bUvFihXJkycPHTp0YNWqVeTNm5f69es/9TrctPas8bBdu3a0adOGDh06YLPZ+Pbbb/n444+ZOXMm4J19+rmYYWrQoAG7du3i0KFDrmWXLl3ixo0bXLt2DUVRAOPi3AMHDgDGdOnBgwcJCQnBYrFw+/ZtALcn582bN13Lw8LC3C5Y9ZRixYoRExPD/Pnznziy+Pnnn+nfvz8LFy4EcM1EPeKJo9bg4GBiY2NZsGBBsheqDho0iFu3brFo0aJk70/Xdb777juaN29O3rx5yZUrF9999x0LFiygW7dulC1b1tV3+fLlBAYGMmXKFHr37k18fLzrYr3AwEC+/vprOnTokGbbCk/f3qioKIoVK5amvyctrVq1ivbt2/Pdd98xd+5clixZwo4dO/Dx8eHcuXMAHD58GICCBQtSuHBh5s+fz4IFC2jXrh1FixZNz/huduzYga+vLzlz5iQ0NJRNmzbhcDgAuHz5MjabjaxZs9KiRQuWLl3K3bt3AaPYHjNmjNsRoyecPn2asWPHkpCQAECBAgWSndmy2WwMGjSI69evA5A9e3ayZcvmlRcOSPn526xZMyZOnEj58uVd4yTA6tWrXTOAmqZRrFgxr2VOql69emzbto3Lly8Dxrg9ceJEzpw549bPZrMxf/581+zGI5qmMX78eNavX++xWYNnKViwIM2bN2fBggV8++23NG3alIwZM6a4ntlspmHDhsyaNYtChQqlWGCllaR/f4CAgAAsFgs7duygRo0aANSpU4c5c+Y89XQcGIWqj48PTqcTMN74sGHDBn777Tc6derk2Q146Fnj4dy5c10Fv8VioUiRIl7fp5+LGSZ/f39mzZrFlClT+Oyzz3A4HJhMJsaPH++acgbjybd37146d+6M3W6nadOmhIaG0rFjR9577z1+++03t6v3LRYL48eP5/r165QtW9YrR4QA7du3Z/Lkya6p/kfKlClDr169yJQpE/7+/tStW9dVPIFREA4dOjTN303RrFkzVq5cSYECBdxmgJJSVZUJEybw8ssv07BhQ4KCglxtj6bHFUXB4XBQo0YNOnTogKIovPLKK3Tv3h2n00mePHl48cUXXetVr16dIUOGcODAAaxWKyEhIdy6dYugoCA6derERx99xOTJk9N0W5+2vVu2bKFPnz5p/nvSytKlS/n0009dt61WK40bNyZbtmy89957+Pn5YTabCQoKonjx4lSvXp2uXbtis9koU6aM29/Kkx6dkksqa9asTJ48mW+//RZVVfH39+fzzz8HoGbNmoSFhdGuXTsCAgIQQjBp0iQA8ubNy7Bhw3j77bfRNI2YmBg6dOjACy+84NFtaNy4MefPn6djx474+fkhhGD48OFs2LDBtR2PVK5cmQEDBjBq1CjefvttTCYTTqeTunXrUqtWLY/mTCq552/Tpk2ZMGGC27UmYBwAjR8/ntatW2O1WvHz82PChAmu9t69e7u9S65Hjx4eOd0SEBDAxIkTGTVqFEIIYmJiqFevHnXq1GHKlClu40rLli1dL+xJ+fr6MmHCBEaMGEGVKlXw8/NL85xP06VLF0aNGkW3bt2Ijo7mpZdeeuY7gx/XsWNHmjdvznfffefhlMmrUqUKe/bsITAwEDCek8OGDXN7jXl0Sk5RFOLi4ujUqZPrEoCMGTNSoEAB7ty54zrT42nPGg9z5szJX3/9xaJFi/D19SVz5sxef3ezIrx1Mj4d1KxZ0+2aGun5sWbNGs6ePev29lvJ3Y8//siLL75IlixZmDZtGmazmbfffju9Y0mSJP1Pei5mmKT/LVOnTmX//v189dVX6R3luZY1a1Z69+6Nn58fgYGBTJw4Mb0jSZIk/c/6r55hkiRJkiRJSgvPxUXfkiRJkiRJzzNZMEmSJEmSJKVAFkySJEmSJEkpkAWTJEmSJElSCmTBJEmSJEmSlAJZMEmSJEmSJKXg/wDAmv91Nv9qNgAAAABJRU5ErkJggg=="/>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>The relationship between eTIV and ASF is almost perfectly correlated negatively, which may be the cause of the high correlation</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [120]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">dementia</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s2">"eTIV"</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">"ASF"</span><span class="p">);</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
    <img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAYcAAAEECAYAAADDOvgIAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAA0dklEQVR4nO3de2DT5f3o8Xfu9zYtDQItLQKtIlClLYpTUOEoOxteKCK0WnVe2Dw74HBHcXJzIirj8hvicIMxdZ2AoCiIm7sg2m2CExQKCApFgTIuLW1pkzaXJt/zR2lsSIsFmqZpP69/NGno95O0zSfP83mez6NSFEVBCCGEaEId7QCEEEJ0PJIchBBChJHkIIQQIowkByGEEGEkOQghhAijjXYAbSUQCOD3R3bhlUajivg12orEGhmxEmusxAkSa6S0JlZFUdDrm08DnSY5+P0KVVW1Eb2G3W6O+DXaisQaGbESa6zECRJrpLQ2VofD1uz9Mq0khBAijCQHIYQQYSQ5CCGECCPJQQghRBhJDkIIIcJ07eSggjJ3PXtP1VLm9oMq2gEJIUTH0OZLWX0+H0899RRHjx7F6/XyyCOP0L9/f5588klUKhXp6enMnj0btVrNmjVrWL16NVqtlkceeYSbbroJt9vN448/zqlTp7BYLMybN4/ExMS2DhNUsLW0msffKsbtC2DUqZk/LpNhKXEQG8uYhRAiYtp85LBhwwbsdjsrV65k+fLlzJkzh+eff56f/exnrFy5EkVR2LRpE2VlZRQWFrJ69WpWrFjBokWL8Hq9rFq1ioyMDFauXMkdd9zB0qVL2zpEAMrq6oOJAcDtC/D4W8WU1dVH5HpCCBFL2jw5fP/73+fRRx8N3tZoNOzZs4err74agBEjRvDxxx9TXFzMkCFD0Ov12Gw2UlNT2bdvH9u3b2f48OHBx27ZsqWtQwSg3OUNJoZGbl+Acpc3ItcTQohY0ubTShaLBQCn08mUKVP42c9+xrx581CpVMGv19TU4HQ6sdlsIf/O6XSG3N/42NbQaFTY7eZWx9krAEadOiRBGHVq9HotpwPQ225CrQ4tQmg06vO6RjRJrJERK7HGSpwgsUbKxcYakfYZx44d46c//Sn5+fnceuutzJ8/P/g1l8tFXFwcVqsVl8sVcr/NZgu5v/GxrXG+7TPiNTB/XGZIzeHRUelMfWMHlbXeZusPnXHrfEcgsba9WIkTJNZI6XDtM8rLy3nggQd4/PHHufPOOwG44oor+OSTTwAoKioiJyeHzMxMtm/fjsfjoaamhpKSEjIyMsjKyuKjjz4KPjY7O7utQ2ygwLCUONZNGsaKe7OZNKIvf9xyiGOn3VJ/EEJ0eW0+cvjtb39LdXU1S5cuDRaTp0+fzrPPPsuiRYvo27cvo0ePRqPRUFBQQH5+PoqiMHXqVAwGA3l5eUybNo28vDx0Oh0LFy5s6xC/pYDDqKXc5eXFTQdCvtRYf3AYO01vQiGEaDWVoiidYuGmz+e/4OFemdtP7rItYfWHdZOGhSSHzjik7Agk1rYXK3GCxBopHW5aKRY5TBrmj8vEqGt4ORr3PDhMMmoQQnRN8u4HIfWHcpeXJIu+ITF0ijGVEEKcP0kOjc7UH4LTSI2JQdWwYa7c5aVXoGGVkyQNIURnJ8nhXKTFhhCii5KawzlIiw0hRFclyeEcpMWGEKKrkuRwDkkWQ3AFUyOjTk2SRR+liIQQon1IcjiHFpe4mrVyDoQQolOTgvS5nLXEtVeCmXgtbD0SWqR+ITeT61LjIPDd31IIIWKBjBy+y5klrgO6mUlLNFNWG16kfnJdMfsq3DKCEEJ0GpIcztN/azzNFqmPVdXJKiYhRKchyeE8WQyaZovUJr1WVjEJIToNSQ7nKdGo49FR6SFF6kdHpXOsqhadVi0FaiFEpyAF6fOUaNDQN8nCpBF9CSigVoFFrwHgsbXFLR4UJIQQsUSSw/lSIKuHld7xRo7VeDDqNOz572le+fgQAA9e35f9ZU5S7CZSrDpJEEKImCTTShfizAqmTIcFvz/Ac3/5EoCCYWms+NdBXtx0gLwVn7C1tFqmmIQQMUmSw0Vq3EWdm5XCix/sD+vDdMTpkwQhhIg5khwuUuMuao2aZpe4fri/TEYQQoiYI8nhYp3ZRX1TuqPZJa7+ANLJVQgRcyQ5tAUFUqy6sD5MU0ams+6zUunkKoSIObJaqa2cGUGsfPAaPtxfhj8AhVsPcey0Wzq5CiFijowc2pICva060h1WVvzrYDAxzB+X2XAmtRBCxAh5x2prZ3VyTbLoGxKD7HcQQsQQSQ6RcGYfhMOoDd4WQohYItNKQgghwkhyEEIIEUaSQzSpkONGhRAdktQcokUFW0urWfD3LxmTmYxGDTmpCQxIMslxo0KIqJORQ5SU1dWz4O9fMiEnlY3FR/EHYNvhSr4or5OfihAi6mTkECXlLi9jMpN5Y9thJuSkBpv2GXVqnh87mOvT4mUEIYSIGvmMGiVJFgMaNYzJTA7r5vqLt3exR0YQQogokrefKHGYNOSkJrTYzfWzw5XsO+WWn5AQIipkWilaFBiQZEKhoUlf0wRh1Knp393G6TofB6vV9E3Qgy96oQohuh75XBpNAbgiycTcsYNDurnOHjOQhX/bx/9d9Tn3/eE/bN5fBbrohiqE6Fpk5BBtAcjsaeV/7rqKvcer6d/dxsK/7ePQqTqgYYpp1obdvPqjofSzG8Af5XiFEF2CJIcOwK7ToD6zAa7OUx9MDAA9443kZqVQVuNBrVJxaZxeVjEJISIuYtNKO3fupKCgAIC9e/dy1113kZeXxy9+8QsCgYZ3tzVr1pCbm8tdd93F5s2bAXC73UyePJn8/HwefvhhKioqIhVix6FAVg8r3x/QneQEU3CKqWe8kYJhaaz410Emr9rBvX/4Dx9+XSWTgUKIiIvI28zy5cuZMWMGHo8HgJdeeomf/vSnrFq1Cq/Xy4cffkhZWRmFhYWsXr2aFStWsGjRIrxeL6tWrSIjI4OVK1dyxx13sHTp0kiE2PEo4DBoucxh5JnbBmHUqcnNSglb5jpz/W6+qfZKghBCRFRE3mJSU1NZsmRJ8PaAAQOoqqpCURRcLhdarZbi4mKGDBmCXq/HZrORmprKvn372L59O8OHDwdgxIgRbNmyJRIhdlw+uCndzqs/GsrlPazNLnP954FyGUEIISIqIjWH0aNHU1paGrzdp08fnnnmGV5++WVsNhvXXHMN77//PjabLfgYi8WC0+nE6XQG77dYLNTU1LTqmhqNCrvd3LZPJOwa6ohfo9GVBgO7VDXNLnP1B2Dm+t289qOr6WbR09tuQq0O7drXnrFeLIm17cVKnCCxRsrFxtouBem5c+fy+uuvk56ezuuvv84LL7zA9ddfj8vlCj7G5XJhs9mwWq3B+10uF3Fxca26ht+vUFVVG5H4G9nt5ohfo6lL4/TMuX0QM9fvDrbWmDIyncKth3D7AhyvdvNxSTmXXxJHTrI1pFDd3rFeDIm17cVKnCCxRkprY3U4bM3e3y4TE/Hx8VitVgC6d+9OdXU1mZmZbN++HY/HQ01NDSUlJWRkZJCVlcVHH30EQFFREdnZ2e0RYscUgBsvtVP4wNVMGdWfB6/vS+HWQ8GzqVUqFb8rOsg3FS72V7ql5bcQos20y8jh2WefZerUqWi1WnQ6HXPmzMHhcFBQUEB+fj6KojB16lQMBgN5eXlMmzaNvLw8dDodCxcubI8QO64A9InT802COWQEMXvMQH5fVILbF2Dxpv0suPNKygxNjiYVQoiLoFIUpVOccOzz+TvdtFIINRyp8fHf024CwO+LSig+Wh388pK8IWjVkGY34zBpsMd3vuFvRxArscZKnCCxRsrFTivJx8xYEYDeFh1GrZrc320JK1KXVtYy7/0vMerUzB+XyS02UxSDFULEOlkMGWMcRg3zx2WG9GJ67OYM/rLrGD+9qT8PDe/LgTInR0/Xfcd3EkKIlsnIIdYoMCwljnWThnGsxoNeq2b+X7/k+4N68uIH+0kw6xmfk8Lu/1bTP8mCw6iBTjFxKIRoT5IcYpECDmND8bnM7efGy7sHE0PBsLSQU+VeGJvJdWlx0o9JCHFeZFopxjlMGtK7N+ykbq7dxpNvF/PFqTpKa33y0xZCtJq8XcQ6Bfp1s5zZ99D8qXKfflNJ3u8/kZYbQohWk7eKTqCxSK1RESxUNzLq1CjKt037jtTIkXJCiO8mNYfO4EyROsNhIa2bhafe3hXWbqPxXIijp+swatVSqBZCnJMkh85CgUS9huFp8fzunmyq3fXsP1lD4dZDAPxkRF9O1Xr58oSTAyedXNEzjqweVkkQQohmSXLobAJwRTcTLgXqfH4qa708OiqdWp+fZUUHgyOKR0elc4nNQLJVJyuZhBBhpObQGSmQbDczJNnGgjuvZEDPOBZvCl3FtHjTfkqr3BR9cxo0UY5XCNHhSHLoxOw6DYqicLLaHbaKKcGsx6zXcKjCxcHTXtBFKUghRIckyaEzayxUd7eGrGLqGW/k3mvT+OXGPfgD8O8D5ew6Vkstfmn7LYQAJDl0fgokW3Qh/ZjG56Sw+tPDTMhJZcW/DrJ2Wyk7SqvYcdTF1zVemWYSQkhBukto7Mf042EcKK+lzudnTGZyiy035tw+iBv720G2RAjRZcnIoatQwGHQcm1qHH2SLGjUtNhyY+b63XxV7pE6hBBdmIwcuho/9E3Q40qxN9tyo3Gz3CmXhxK1in4JeqiPYrxCiKiQkUNX5IPBPc08N3ZwSMuNnvFGCoalsbH4KF8ed/JxSTm7TtTKRwghuiD5s++qfDC8Tzy94g0kJ5iZtX43uVkpvLGtoVDdtAbx3NjBDOxhJVEvLTeE6CokOXRlfugXb6SbRccf7hvKKZcXSA6rQTz19i4mjehL325WORtCiC5CppW6OgXsGg3pSQYcNkOwUN2U2xcgoNBwNkR5neyFEKILkOQgGvigX4Keq3rbm237bTdpWTT+Smrc9ZRUe6jyy4Y5ITozmVYS36qHwZc0FKqbtv3+f7dcRjernsfW7gzeN/vWgXS36cnsbpFpJiE6IUkOIlQ9DE+LZ9VD13C4so6SMie9E808uvpz3L4APeON3H1NKmoV6LUajjh99JbOrkJ0OpIcRLgApJh1pFh12E06Ttf5gonh/u/14X/+8RUJZj3jc1JITTTj8hi43GGS/RBCdCKSHETLzpwN8U2NBqNOTW5WSjAxnN1y47mxgxneN15abgjRSUhBWpybAn3i9Txz+6Bzttx46u1d7D5ey3FPvfxWCdEJyJ+x+G5+uKmfnev7JzXbcgMabn9+pIq/7z3Jh19XSV8mIWKcJAfROvVwaYKeObcPCmm50cioU+MPQECBmet3U1LhkUlLIWKYJAfRej64sZ+dkZd159k7BgUThFGnZsrIdDYWH0VRGkYRH5ecoujr01R4ZT+EELFIPtuJ81MPvUxaevWz8/I92Xx+uBJ/gGBPpsKth4KjiOlv72LBnVei06jI6mGVvkxCxBBJDuLC+GCQw4RWpeJEjZvbr0qmcOshKmu9TBmZTuHWQ7h9Ab46WYNJp6FPgqmhcZ8QIiZIchAXzg+XJxrpbtORbDc13BWAwq2HOHbaHRxBLN60n6tS4iU5CBFDpOYgLo4CiVoN/RMN9OlmYcW/DgYTw5SR6az7rBS3L0Ct1x/tSIUQ50FGDqJt1MPw1HhWPngNH+4vCxtB9IwzUOaup9zlJcliwGGSsyGE6MgkOYi2o0Bvq450h5XH3yoO7p6ePy6TI1VuHn1jR7DtRj+HlbQEE8lW2RAhREckyUG0LQWGpcSxbtKwM6MEPRq1itt/u6XZthtzbh9EVm+FOI1KRhJCdCARqzns3LmTgoICAE6dOsUjjzzC3XffzcSJEzl8+DAAa9asITc3l7vuuovNmzcD4Ha7mTx5Mvn5+Tz88MNUVFREKkQRKQo4jFoGdDPjMGo5UeNpse3GzPW7WV98jK2l1bIfQogOJCIjh+XLl7NhwwZMpoYVLPPnz+fWW2/lBz/4AVu3buXgwYOYTCYKCwt566238Hg85Ofnc91117Fq1SoyMjKYPHky7733HkuXLmXGjBmRCFO0kySL4ZxtN7RqNfvLnOi0ai6xGkixSQtwIaItIskhNTWVJUuW8MQTTwDw2Wefcdlll3H//feTnJzM9OnT2bJlC0OGDEGv16PX60lNTWXfvn1s376dhx56CIARI0awdOnSVl1To1Fht5sj8XSaXEMd8Wu0lY4Ua1xAYeH4q/jqRDVGnTokQRh1avp3t/LYmh3Bqaa5YwfzgwHd0Wo73tLXjvS6nkusxAkSa6RcbKwRSQ6jR4+mtLQ0ePvo0aPExcXx6quv8tJLL7F8+XL69OmDzWYLPsZiseB0OnE6ncH7LRYLNTU1rbqm369QVVXbtk/kLHa7OeLXaCsdLdare1np381ESoKZmet3BxPBzDFXMO/9vSFTTdPf3kU3SzYDu5k6XB2io72uLYmVOEFijZTWxupw2Jq9/5w1hyeeeIJt27ZdWGRN2O12Ro4cCcDIkSPZvXs3VqsVl8sVfIzL5cJms4Xc73K5iIuLu+jriw5AgUS9hhv72vnjA1ezYHwmk0b0pcbt49CpupCHun0BPjtcSanLJ3UIIaLknMnhlltu4fe//z233XYbr732GqdPn76gi2RnZ/PRRx8B8Omnn9K/f38yMzPZvn07Ho+HmpoaSkpKyMjIICsrK/jYoqIisrOzL+iaooPyw6Vxeiy6himjZLu5xQ6v+086pVAtRJSoFEX5zoF7eXk577zzDu+99x79+/dnwoQJ5OTknPPflJaW8thjj7FmzRqOHj3KjBkzqKurw2q1snDhQuLj41mzZg1vvPEGiqLw4x//mNGjR1NXV8e0adMoKytDp9OxcOFCHA7Hdz4Rn88v00pNdPhYVVBWV095rZeTTh8z3tkVnGqaMjKdN7YdZu7YQQQCcLqunh5xBvrY9VE/irTDv65nxEqcILFGysVOK7UqOTTyeDwsXbqUP/zhD+zatav1UbYDSQ6hYiZWFXzj9FBe42Pv8Wr8AdhYfJSf35yO26cwa8OeYNJ45rZB3NTfHtUEESuva6zECRJrpES05tBo27ZtzJw5k7Fjx6IoCu+99975RSlESxQY3CMeznxGUang9quScdhMwcQADXWIWRt2s6/cTZlHzogQItLOuVrpxRdfZOPGjfTp04fx48cze/ZstFrZVC3alkajJqeXjbQEEyUVtew/6eTkmY1zTSWY9fjqA+w+Vk3PeBOXJxlB+vkJERHf+U7/2muv0bNnz/aIRXRlZ3ZVO5Lj6JdopqY+ELInome8kXuvTeP/rPwsOM307B2DyOhupadZK5vmhGhj50wO3bt3p6ioqNmvTZgwISIBiS6uMUlo4ZnbBjFrQ8OeiPE5KSzeFNp6Y8Y7u1lw55V8U6Fwbe84GUUI0YbOmRzKy8vbKw4hQtXDTf0b9kScqPZQ66lvtvVG40lzR+JN9Ja2G0K0mXMmh8GDB3PDDTe0VyxChKpv2BNR5/Nz4GRNs603Gk+aW1aQzZYjdaQ2tgGXJCHERTnnaqUVK1a0VxxCNC8AVySZuOwSG4+OSg9umDv7pLnjp91MWb2Dib//hKJvTkPHa8skREw558hBURR8Ph/NbYXQ6/URC0qIEH4Y2stGv25mslLt/LvkVNhJcydrPPSMN5KblcKhChf77UbS7QYZQQhxgc6ZHHbu3Mn3v/99FEVBpWpYWN74/5s2bWqXAIUAgr2ZEs0ajiSamfHOt837pv6vDN4r/m/IQULLig42rGZyWOlpkdVMQpyvcyaHK6+8ksLCwvaKRYjvVg839LPzyv1DOVnjIcGsY+b63YzJTA47SGjJB/t5buxg/lvtJjXBhMMg51YL0VrndRLchTbeE6JN+aB/vIHLHRZMOjVTRmWgUYceJNQz3siEnFSeensXu45W8/4XJ/jiVJ3UIoRopXMmh5kzZwLwn//8hzFjxjBx4kQWL17M2rVr2yU4IVp0Zpqpj9XAiD7xDOvbLaS7a25WCm9sO8yEnFQ+OVjGgB5xVLvr2Vfu5rinPoIH5ArROZzzTyQjIwOAxYsX86c//YmkpCR+8pOfsGrVqnYJTohW8UO63cALYwcHE4RGDWMyk/lg33HuzE5l6podTF71OQ8XbmPvsRq+rvGALspxC9GBtapRklqtxm63o1KpMBgMWCyWSMclxPkJwHWp8az78TAOV7mpDyh8daKGe7/Xlyfe3HlWA789TBrRl28SzGQm2+im10jBWoiztGpwnZqaysKFC6mqqmLZsmX06tUr0nEJcf4UcBi0ZKdYCSgKA3rGUedtfmd1QIFZ63dTUVvP19VeGUUIcZZWJYdf/vKX9OrVi+zsbEwmE3PmzIl0XEJcOB9c2zuOlHgjvRObP2lOURqSxJGKWu79w3/YvL+KMp9fCtZCnNGqaSWtVkteXl6kYxGi7fihh1FLD5uWObcPYub63SEnzRVuPYRRp8ak1wbPilian8XJGhUDLzGBL9pPQIjoksMZROfmgxv721n50DUcqayjpMxJ4dZDVNZ6mT1mIL8vKgEaRhGfHani9/88yLN3DOaKXlYcJo0kCdFlSXIQnZ8Pelt0dLOo6RlnJOMSGyiwrKiE4qPVQOhU04x3dvHbe7KpqlWTYtdiUmTznOh6ZLW36BoUMCsaLrXriTNqcHnr+eqkEwht4gcNCWLboUoeePVTPv3GSUV9vRxLKrocGTmIrsUPAxLNJMcb+OOPruaUy8ve49XBJn4QOoqY/s4uXr47G3+cqqH9hhBdhCQH0fUoEKfWEBevIcGiweX1U1nrBQgpWENDgvj8SCXX9evGyRov3uMuUuxG6dMkOj1JDqLrCoBdreGGfvH88YGrqXB5+eJY+CjCH4Dj1R6mvVUcXPE0LzeT76XGyeY50WlJzUEIH1xq15OWaCIt0RI2ithYfJSSMmfILutp64rZX+mhOuCXeoTolGTkIARAPSTpNIzoF8/Ld2fz+ZFK/AF4Y9th/u9N6Sz6+1chD3f7Anx2uJKByfHUeevpk2DGYZSpJtF5yMhBiKZ8MKiHiev7J3F5Dysv5GYSCHxbk2hk1Knp57Dymw++oj4Au45Vc+C0NPMTnYckByHO5oNLrXqG9Y5Dp1FhMujCzq9++taBvP35Ye6+pg9HK2tRq1TUef3sl5bgopOQaSUhWuKHNKue7lYNPeKNLCvI5vhpNydrPJh0asZlp3HolIvFm/YHC9Uzx1xBglmHy6unX4IB6qP9JIS4MPL5RohzUcCkaLg0Xk+CSYdGo+alzQdQq9Xo1CoW/f2rkEL1nI1fsOe/Ndz/yqdsLqmiyi8FaxGbJDkI0Rr1DY38Rg9I4uV7sjHo1HjqA822A1epGv77m837OVbtZUtpNWUeSRIitsi0khDnwaDVMchh4qiznlpfPUadOiRBNO6ubjzDelLh9uCU0wu5g7kuLR78UXwCQrSSjByEOF9+SDZpSU808nyTo0mb9mjKzUrhxQ/2h0w5PbluFyWVHvlIJmKC/JoKcaHq4fq0eFY9dA0nnR50GjW/fHcPx0670agJm3JKMOup9frZcqiaHvEG4vVaEqUNh+igJDkIcTECkGLWkWLRUV3v5/ncTMpqPHS3GVhWdDCYIHrGG7n32jT+z8rPSDDrGZ+TQj+HlZ7xRhJMGuxaSRKiY5HkIERbUCBOoyEuQYNRq6ZeUXh0VHpwmev4nBQWb9pPgllPwbC04JSTUadmzu2D6Oew0Numk3qE6DAkOQjRlvwNBwtV1/tJSzQzaURfAgok2024fYFmaxEz1+9m0oi+pHWzcFWylTiNjCJE9EWsIL1z504KCgpC7nv33XeZMGFC8PaaNWvIzc3lrrvuYvPmzQC43W4mT55Mfn4+Dz/8MBUVFZEKUYjIODOKGNrLxvev6E5GdysWgxajTh1c5tqU2xcgOd7EoVMuTjjrOVjtkaUiIuoi8iu4fPlyZsyYgcfjCd63d+9e3nzzTRSl4SNRWVkZhYWFrF69mhUrVrBo0SK8Xi+rVq0iIyODlStXcscdd7B06dJIhChE5Cng0Gu5NjWOBLOOZ24biEZFcHVTI6NOzdHTdby46QAPvPopB8pcbD/m5BunlzKfXxKFiIqITCulpqayZMkSnnjiCQAqKytZsGABTz31FDNnzgSguLiYIUOGoNfr0ev1pKamsm/fPrZv385DDz0EwIgRI1qdHDQaFXa7ORJPp8k11BG/RluRWCPjQmPNsZhIjjdyrNpESoKZmet3B2sOj45K549bvj1caM7GL3jw+r6s+NdBfnnbQBLMekb064ZG0/os0RVe02joSrFGJDmMHj2a0tKG83j9fj/Tp0/nqaeewmAwBB/jdDqx2WzB2xaLBafTGXK/xWKhpqamVdf0+xWqqmrb8FmEs9vNEb9GW5FYI+NiYrUA/eONdLfoeOX+oZys8aBRqZj7573Bw4UgdJf17A17WHDnlew4epoEk5ZEfevqEV3lNW1vnTFWh8PW7P0RL0jv2bOHQ4cO8fTTT+PxeDhw4ABz585l2LBhuFyu4ONcLhc2mw2r1Rq83+VyERcXF+kQhWg/jaua7BrsJi2Vdb5m24GfmX3F7QtgNWoIAPvLaukeZ8Bh1mCVorWIsIgnh8zMTN577z0ASktLeeyxx5g+fTplZWX8+te/xuPx4PV6KSkpISMjg6ysLD766CMyMzMpKioiOzs70iEK0f4CDYcLJZk1PD92ML94e1dwmqnpGdY5afGcqPYwe8Oe4NefuW0QPeL0DEgyyzGlImKitpTV4XBQUFBAfn4+iqIwdepUDAYDeXl5TJs2jby8PHQ6HQsXLoxWiEJEnq9hl/Xqh67heI0HrUbNnI0Nu6wb6hGX8XDhtuAKpwSzntKqWuJMWg6e9tLXrpe9ESIiVErj8qEY5/P5pebQhMQaGRGNVQUVXj9lLh81nnoseg3Hqz088WYx0LDL+uwNdM/cNogBPaz0sGhDkoS8ppHRGWNtqeYgi+SE6CgUSNRpuMxuJKenFX9AwazXBJe+NreBbtaG3RyqqOOjr6soqfZwtM4nW1tFm5DkIERHFIBB3c0YtWpm3zrwnBvo3PV+DlfUUub0UOcL8MmRGvYcq5a/bnFR5NdHiI7KD1d2t5DTO45X7x/K1X0Smt1AZzfrWb/jKEcq6nhyXTF7j9XwwZcn2VNWhzMghwyJCyMDUCE6MgXsWg32OA1oYM7tg0I20D17xyDmbNzDmMxk3th2mAk5qSE1ibljB5Ng1tLDasRhlOWvovUkOQgRK/xw46V2Vj54DUdP16FCxYlqN4dO1aFSwZjM5LCaxPS3dzH/ziv565ETDOgRR3Yvqyx/Fa0i00pCxJJAQ9fXYb3j6BlvpH93a3CqqbkDhty+AF+eqOF3RQf5+pSLg6c9HHJ65WOh+E6SHISIRX5Itei4oruJ58YO5t2dRxnQI67ZmoSiNCSJxZv2Ux9QOF7tYevhGkrrfKCLUvyiw5PPD0LEsnoYnhbPpXddRbXbx9yxg5newm7rBLOeb07VMmfjFyEHDWUm20jUST1ChJLkIESsO3NUKRYd1fF+Xrl/KNV1PvYcq6Zw66FgU7/xOSnBxAChBw31TjDT32EhJU4H9dF8MqKjkGklITqLM039+scbGJhspXeCOdjUz6hT0zvB3GxNIqDAzPW7OVrl5uND1Q0b6eSdocuTkYMQnY0Cl1jN3Ngf/vjA1Zxyetl7vJqTNQ39mpomiKY1ia9O1vDipgMYdWqeGzuYnFQrJmS6qauSzwdCdFY+uNSqJ6eXlX4OK2u2HWHKyPRg0bqxJrHus1KMOjX+MznD7Qvw1Nu7OFLlY/txJ6W1MpLoimTkIERnF4DvpcSRnjeEMpeX1350NSeq3Rwoc1K49RCVtd6QwjU0JIhPvq4IjiTm3D6IGy+1yx6JLkSSgxBdgQIOgxaHQQsqsBs09Igz0M9hRaNSMf9v+0JOozt7JDFz/W5WPngNvS2y9rWrkMGiEF2NAol6DZfaDHyvTxyXxBt4dFRGs9NNjdy+ABW1Xso89Xx+0sneyjqO1vpAE60nISJNRg5CdGU+6GPV092iYWl+FjtKq0jvbmPBWSOJtG4matz15K76PLhH4rGbMxjQ04YSUEgyG3CYpHjdmcjIQYiuTgEzGgb3NHN9/yQMWjVTzhpJzBozMHiUKTSMJBb9/Sv2/reaT76p4v19J9h7qk7eUToRGTkIIRqcWd1EvJ4jNT5W3JdDhcuHXqPGU+8P2yORYNZjMepY9I/9JJj1AFTV+eifZJEOsJ2AJAchRCh/Q3O/sjoV/voASRY9qFRheyQad1wnmPVhx5fOvWMwg3pYSTRIkohVMggUQoRTwGHUMqCbGYdRi8OoYf64zJCpptTEhh3XzR1fOv2dXXxdUcdXVW52nHQ1FK/l3SamyMhBCPHdFBiWEse6nwzjcKUbk04DKs55fKnTU8/P1uwIOZjohj522SsRIySXCyFaRwGHXkt2DysOs46AEmDu2MFoziSJpow6NYcra0NGEzPe2c3+Sjdlbjm6NBZIchBCnJ8zU06DulnI7GllaJ9EZo65ImTKaeaYK1i7rTTkn7l9AY5U1JG7bAtbS6slQXRwMq0khLgwjedbJ2hwmHW8dv9QTtX62He8mhq3L9gRtpFRp8Zs0OL2BVjw9y9ZcOeVlDs99HL76WXWyHRTByPJQQhxcc7suE7Ua+ibYKDO5+fFTV8xZWR6yAqmx27OoLSylp7xRibkpFLwh/+ErG7qFacn3qiXzXQdhEpRlE7xY/D5/FRV1Ub0Gna7OeLXaCsSa2TESqxRjVMNR50+ymu96DVqTtZ4KKvxYNZp+G3RQXKzUljxr4NhrcMfvL4vK/51kBfGZnJdWlyHHEnEys8fWh+rw2Fr9n4ZOQgh2lYAks06ki06yurqIaDgsBqYtWE3x0670aibX92kUjVsrDt4yolep6ZPgkk200WRJAchRGScKVw7jA2dYF+eOIRylxezQcuyovCRg1GrDtlMl5MWz2M3X87pOi89bEZSbLoOOZrorCQ5CCEir2miUMOc2wcxc/3uYM1hysh0VCpYvKkhMWQmxzEuK5UHXvs0+Bg5U6J9SXIQQrSvANx4qZ2VD17DSacHo07D7A27ufXK5OBo4qER/XjizZ0h+yRmrt9N4QNXU+epJ8kiXWAjTZKDEKL9BRr6N/W26LDZjDxz2yBqPPXB/k11nvpm6xJfl7v4n3/sZ3xOCundrfTrJk3+IkU2wQkhokqjUXNFNxPp3czMvWNwcD9Ec7uurQYtBcPSWFZ0kMmrdpD7O9lQFymSHIQQ0Xdmr8SItHjWTRpGD5uOObcPCtl1PXvMQMqdnrAmf4+/VUxZXT1l7nr2nqqV9hxtRKaVhBAdR5PCdZ94IysfvIYTNW6SrAbmvb+XYf0czU43lVTU8vibxSSY9TLl1EYkOQghOqYmdQlUcN+1l3KgzBl2roRRp2b/SWez50rMH5fJsJQ4SRAXQKaVhBAd35mW4T+44pJgXQIItt5Yu6202XMlHn+rmAqPnzJ3PTvLXByodlPhlWmn1ojYyGHnzp0sWLCAwsJC9u7dy5w5c9BoNOj1eubNm0dSUhJr1qxh9erVaLVaHnnkEW666SbcbjePP/44p06dwmKxMG/ePBITEyMVphAiVpxVlyh3eUmy6NGoVVTWeps9VyLBrGf3cSfT39kVHE08OiqdvkkWsnpYZURxDhEZOSxfvpwZM2bg8XgAmDt3LjNnzqSwsJCbb76Z5cuXU1ZWRmFhIatXr2bFihUsWrQIr9fLqlWryMjIYOXKldxxxx0sXbo0EiEKIWLVWafUJRoaTqlr7lyJ8TkpwcQADclj8ab9+PwKxSddlLp8HKiqkyJ2MyIyckhNTWXJkiU88cQTACxatIju3bsD4Pf7MRgMFBcXM2TIEPR6PXq9ntTUVPbt28f27dt56KGHABgxYkSrk4NGo8JuN0fi6TS5hjri12grEmtkxEqssRIntE2st9hMDOwVR1o3C0+9/e0oIb27rdkC9lcna3hx04Hg7uw3th3midED+F+XOVCrW84SXel1jUhyGD16NKWl3x700ZgYPvvsM/70pz/x+uuv889//hOb7dtugBaLBafTidPpDN5vsVioqalp1TX9fkW6sjYhsUZGrMQaK3FC28VqU8Hw1NApJ1SqZgvY/jM33b4AL36wnwev78vP1+5g3aRhDS0+Ihxre7jYrqztVpD+85//zOzZs1m2bBmJiYlYrVZcLlfw6y6XC5vNFnK/y+UiLi6uvUIUQsS6s6acHMaGKaemBewpI9NZ99m3H14bO8K6fQHKXV5QIXsmaKelrOvXr+eNN96gsLAQu90OQGZmJr/+9a/xeDx4vV5KSkrIyMggKyuLjz76iMzMTIqKisjOzm6PEIUQndGZVU7rJg3jWI0Hq1HLE28Vc+y0O/gQo06NojT8N8miZ2tpNY+/VRycmnph7GAusTUcRBQX6DoV7IgnB7/fz9y5c+nZsyeTJ08GYOjQoUyZMoWCggLy8/NRFIWpU6diMBjIy8tj2rRp5OXlodPpWLhwYaRDFEJ0Zme1Dv9/N18W8ubfWHOYPy4TjVoV/Bo0jCaefHsXT/3vy0m01FNSUUuK3UiKtfO3D5eT4M5DZ5xv7Agk1rYXK3FCFGJVQVldPeUuL1ajDo+vnnijDodJy97yWu59dVvIwzOT47h7WBqzN+wJaR/eJ9GIRafrsN1hY6bmIIQQHUKTukRvi47+dlPDqEKBJIshbDnspBH9gokBvm0ffqzGxyOrP+OLU3Wdsj4h7TOEEOIMh6mhgN102smvKM0uh1WUABNyUvnxn7Y3W5/oqCOK1pLkIIQQjZoUsMtdXhSVijqfv9nlsHaznmlv7QqrTzx4fV9W/Osgc+8YzKAeVhINsZkkZFpJCCGaajLtdEU3E/26mXimmfbhe/9b0+yIonFZ7PR3dvHeFydi9rwJGTkIIURLFLBrNdzU5FjTOKOORX/fx7B+jmZHFI1LfNy+AAEFFvz9S/5n/FU43b6YOt5UkoMQQnyXM+3DByfHU3W6lmfGDOS020f/pME82aRdx5SR6RRuPQQ0JAqjVs2EnFTyV3wSc23EJTkIIcT5aLJvon+CKaQ+MWvDbo6ddgcThUoFizeFtxH/rjYdHUHHjk4IITqyszbYvTxxCCUVtew/6aRw6yHG56Q0W5cod3klOQghRJfQmCiS4+iXaCantx2bUceyooNhdYkki77l79Nkk140axSSHIQQoi2dNZo4e9/E/HGZOEza5t/wVYT1dopWjUKSgxBCRMpZ+yaSLPqWEwMNI4azeztFq0YhyUEIISKp6UjizO2WlLu8HaZGIZvghBCig2iut1OLNYoInzshyUEIITqIxt5OTXdjB2sUTZ2pTeQu28q9r24jd9mWNt+JLdNKQgjRUbSyRtEetQlJDkII0ZG0okbRHrUJmVYSQogYc161iQskyUEIIWJMq2sTF0GmlYQQItac5/6JCyHJQQghYtF57J+4EDKtJIQQIowkByGEEGEkOQghhAgjyUEIIUQYSQ5CCCHCqBRF6eAnmQohhGhvMnIQQggRRpKDEEKIMJIchBBChJHkIIQQIowkByGEEGEkOQghhAgjyUEIIUQYSQ7NCAQCzJo1iwkTJlBQUMChQ4dCvv7OO+9w6623kp+fz9q1a6MU5bd27txJQUFB2P0ffPAB48aNY8KECaxZsyYKkYVrKVaAuro6Jk6cSElJSTtH1byWYt24cSPjx49n4sSJzJo1i0Ag0My/bl8txfrXv/6VcePGceedd3bo39VGM2fOZMGCBe0YUctaivWVV17hhz/8IQUFBRQUFHDw4MEoRBeqpViLi4vJz88nLy+PKVOm4PF4Wv09pWV3M/7xj3/g9Xp544032LFjBy+88AIvv/wyABUVFSxevJi3336buLg47r//fq699lpSUlKiEuvy5cvZsGEDJpMp5H6fz8fzzz/Pm2++iclkIi8vj5tuugmHwxGVOKHlWAF27drF7NmzOXHiRBQiC9dSrG63m1//+te8++67mEwmHnvsMTZv3syoUaOiFGnLsfr9fhYuXMhbb72F2WzmBz/4AaNGjSIxMbFDxdlo9erVfPXVVwwdOrSdIwt3rlj37NnDvHnzGDRoUBQiC9dSrIqiMHPmTF588UXS0tJYu3YtR48epW/fvq36vjJyaMb27dsZPnw4AFdddRW7d+8Ofq20tJTLL78cu92OWq1m8ODB7Ny5M1qhkpqaypIlS8LuLykpITU1lfj4ePR6PdnZ2Wzbti0KEX6rpVgBvF4vv/nNb1r9ixtpLcWq1+tZvXp18A+xvr4eg8HQ3uGFaClWjUbDn//8Z2w2G1VVVQBYLJZ2ju5b5/r5f/755+zcuZMJEya0c1TNO1ese/bsYdmyZeTl5fG73/2unSML11KsX3/9NXa7nddee4177rmHqqqq8/r7kuTQDKfTidVqDd7WaDTU19cDkJaWxoEDBygvL6euro4tW7ZQW1sbrVAZPXo0Wm34ANDpdGKz2YK3LRYLTqezPUML01KsANnZ2fTs2bOdI2pZS7Gq1WqSkpIAKCwspLa2luuuu669wwtxrtdVq9Xyt7/9jdtvv52cnJwWH9ceWorz5MmTvPTSS8yaNSsKUTXvXK/pD3/4Q55++mlee+01tm/fzubNm9s5ulAtxVpZWcnnn39Ofn4+r7zyClu3bmXLli2t/r6SHJphtVpxuVzB24FAIPjix8fH84tf/ILJkyfz1FNPMXDgQBISEqIVaovOfg4ulyskWYgLFwgEmDdvHv/+979ZsmQJKpUq2iGd0y233EJRURE+n4933nkn2uGEef/996msrGTSpEksW7aMjRs3sm7dumiH1SxFUbjvvvtITExEr9dzww038MUXX0Q7rGbZ7XbS0tLo378/Op2O4cOHh8yCfBdJDs3IysqiqKgIgB07dpCRkRH8Wn19PTt37uT1119n3rx5HDx4kKysrGiF2qJ+/fpx6NAhqqqq8Hq9bNu2jSFDhkQ7rE5h1qxZeDweli5d2uL8eUfgdDq555578Hq9qNVqTCYTanXH+5O/9957WbduHYWFhUyaNIkxY8aQm5sb7bCa5XQ6GTNmDC6XC0VR+OSTTzpM7eFsvXv3xuVyBRfUbNu2jfT09Fb/eylIN+Pmm2/m3//+NxMnTkRRFJ577jneffddamtrmTBhAjqdjtzcXAwGAz/60Y+iVuBrTtM4n3zySR588EEURWHcuHFccskl0Q4vRNNYO7rGWAcNGsSbb75JTk4O9913H9Dw5nbzzTdHOcJvNX1db731Vu6++260Wi2XXXYZt912W7TDC4rFn/+ECROYOnUq9957L3q9nmuvvZYbbrgh2uGFaBrr3Llz+fnPf46iKAwZMoQbb7yx1d9HWnYLIYQI0/HGmEIIIaJOkoMQQogwkhyEEEKEkeQghBAijCQHIYQQYWQpqxBtYNmyZfzxj39k06ZNGAwGKioqmD17NrW1tSiKQq9evZgxYwZGo5GRI0fSs2fP4J6D+Ph4XnrppSg/AyFCyVJWIdrArbfeyrXXXsvll19Obm4uv/rVr+jduzd5eXkAzJ07l+TkZO6//35GjhzJX/7yl6j3ZBLiXGRaSYiL9Mknn5CamsrEiRN5/fXXAUhOTuavf/0rH3/8MW63m2nTpp2zVbUQHY1MKwlxkdauXcv48ePp27cver2enTt3kpeXh8FgYMWKFTz66KNkZ2cze/bsYHPBBx54IDit9OCDD57XzlUh2oNMKwlxEU6fPs3NN9/MoEGDUKlUnDx5Mji1NHToULRaLV6vl+XLl7Nv3z6WLFki00oiJsjIQYiLsGHDBsaNG8e0adOAhtPsRo0aRWVlJUeOHOGuu+5Cr9eTnp7eIU4ME6K1JDkIcRHWrl3Lr371q+Btk8nELbfcQo8ePfjwww9ZuXIlRqORhIQEnn766egFKsR5kmklIYQQYWS1khBCiDCSHIQQQoSR5CCEECKMJAchhBBhJDkIIYQII8lBCCFEGEkOQgghwvx/vXVGasroTJMAAAAASUVORK5CYII="/>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>As we can see below whenever the number of visits is 1, the MR Delay equals 0</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [121]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="p">[</span><span class="n">dementia</span><span class="p">[</span><span class="s2">"Visit"</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">][</span><span class="s2">"MR Delay"</span><span class="p">]</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[121]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>139    0
    205    0
    62     0
    320    0
    318    0
    245    0
    218    0
    134    0
    76     0
    39     0
    Name: MR Delay, dtype: int64</pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Dropping highly correlated data</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [122]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s2">"Visit"</span><span class="p">,</span> <span class="s2">"ASF"</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Also whenever the CDR feature equals to 1 or 0 its maps to Demented and Non-demented respectively, this column will be dropped to make the model more intelligent</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [123]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="p">[</span><span class="n">dementia</span><span class="p">[</span><span class="s2">"CDR"</span><span class="p">]</span> <span class="o">==</span> <span class="mi">1</span><span class="p">][</span><span class="s2">"Group"</span><span class="p">]</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[123]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>329    1
    173    1
    88     1
    317    1
    90     1
    238    1
    188    1
    226    1
    186    1
    97     1
    Name: Group, dtype: int64</pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>All patients are right-handed so this feature isnt useful</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [124]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="p">[</span><span class="s2">"Hand"</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[124]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>R    373
    Name: Hand, dtype: int64</pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Data Shuffle</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [125]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span> <span class="o">=</span> <span class="n">dementia</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">frac</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">11</span><span class="p">)</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Dropping unuseful features</p>
    <ul>
    <li>Subject ID - id of pateint</li>
    <li>MRI ID - id of mri scan for each patient</li>
    <li>Hand - all patients are right handed</li>
    </ul>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [126]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s2">"Subject ID"</span><span class="p">,</span> <span class="s2">"MRI ID"</span><span class="p">,</span> <span class="s2">"Hand"</span><span class="p">,</span> <span class="s2">"CDR"</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Focus of pateint is Demented or Not Demented, so converted patients are not needed</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [127]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">mask</span> <span class="o">=</span> <span class="n">dementia</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">dementia</span><span class="p">[</span><span class="s2">"Group"</span><span class="p">]</span> <span class="o">==</span> <span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">index</span>
    <span class="n">dementia</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">mask</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h3 id="Data-Split">Data Split<a class="anchor-link" href="#Data-Split">¶</a></h3>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [128]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
    <span class="n">X</span> <span class="o">=</span> <span class="n">dementia</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s2">"Group"</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span> 
    <span class="n">y</span> <span class="o">=</span> <span class="n">dementia</span><span class="p">[</span><span class="s2">"Group"</span><span class="p">]</span>
    <span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">51</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Rows and instances in train and test set respectively</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [129]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">X_train</span><span class="o">.</span><span class="n">shape</span><span class="p">,</span> <span class="n">X_test</span><span class="o">.</span><span class="n">shape</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[129]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>((268, 8), (68, 8))</pre>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [130]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Renaming X_train to demnetia</span>
    <span class="n">dementia</span> <span class="o">=</span> <span class="n">X_train</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
    <span class="n">dementia</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[130]:</div>
    <div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
    <div>
    <style scoped="">
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
    <thead>
    <tr style="text-align: right;">
    <th></th>
    <th>MR Delay</th>
    <th>M/F</th>
    <th>Age</th>
    <th>EDUC</th>
    <th>SES</th>
    <th>MMSE</th>
    <th>eTIV</th>
    <th>nWBV</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <th>243</th>
    <td>1345</td>
    <td>1</td>
    <td>76</td>
    <td>20</td>
    <td>2.0</td>
    <td>30.0</td>
    <td>1823</td>
    <td>0.739</td>
    </tr>
    <tr>
    <th>224</th>
    <td>675</td>
    <td>1</td>
    <td>87</td>
    <td>12</td>
    <td>4.0</td>
    <td>30.0</td>
    <td>1762</td>
    <td>0.718</td>
    </tr>
    <tr>
    <th>314</th>
    <td>0</td>
    <td>0</td>
    <td>78</td>
    <td>18</td>
    <td>1.0</td>
    <td>30.0</td>
    <td>1243</td>
    <td>0.748</td>
    </tr>
    <tr>
    <th>68</th>
    <td>0</td>
    <td>0</td>
    <td>69</td>
    <td>13</td>
    <td>4.0</td>
    <td>30.0</td>
    <td>1359</td>
    <td>0.789</td>
    </tr>
    <tr>
    <th>142</th>
    <td>451</td>
    <td>1</td>
    <td>68</td>
    <td>12</td>
    <td>4.0</td>
    <td>29.0</td>
    <td>1438</td>
    <td>0.738</td>
    </tr>
    <tr>
    <th>...</th>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    </tr>
    <tr>
    <th>255</th>
    <td>597</td>
    <td>0</td>
    <td>88</td>
    <td>16</td>
    <td>3.0</td>
    <td>30.0</td>
    <td>1295</td>
    <td>0.744</td>
    </tr>
    <tr>
    <th>41</th>
    <td>0</td>
    <td>0</td>
    <td>61</td>
    <td>16</td>
    <td>3.0</td>
    <td>30.0</td>
    <td>1313</td>
    <td>0.805</td>
    </tr>
    <tr>
    <th>276</th>
    <td>539</td>
    <td>0</td>
    <td>71</td>
    <td>11</td>
    <td>4.0</td>
    <td>28.0</td>
    <td>1284</td>
    <td>0.741</td>
    </tr>
    <tr>
    <th>94</th>
    <td>575</td>
    <td>0</td>
    <td>85</td>
    <td>15</td>
    <td>2.0</td>
    <td>22.0</td>
    <td>1483</td>
    <td>0.748</td>
    </tr>
    <tr>
    <th>16</th>
    <td>576</td>
    <td>1</td>
    <td>69</td>
    <td>12</td>
    <td>2.0</td>
    <td>24.0</td>
    <td>1480</td>
    <td>0.791</td>
    </tr>
    </tbody>
    </table>
    <p>268 rows × 8 columns</p>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Extracting numerical features</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [131]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">numerical</span> <span class="o">=</span> <span class="p">[</span><span class="n">col</span> <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="n">dementia</span><span class="o">.</span><span class="n">columns</span> <span class="k">if</span> <span class="n">dementia</span><span class="p">[</span><span class="n">col</span><span class="p">]</span><span class="o">.</span><span class="n">dtype</span> <span class="o">!=</span> <span class="s2">"O"</span><span class="p">]</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h3 id="Missing-data-Imputation">Missing data Imputation<a class="anchor-link" href="#Missing-data-Imputation">¶</a></h3>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Checking features that have missing data</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [132]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[132]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>MR Delay     0
    M/F          0
    Age          0
    EDUC         0
    SES         14
    MMSE         0
    eTIV         0
    nWBV         0
    dtype: int64</pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Importing library used for handling missing data</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [133]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.impute</span> <span class="kn">import</span> <span class="n">SimpleImputer</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Using median to replace missing values as the data contains outliers</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [134]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">imputer</span> <span class="o">=</span> <span class="n">SimpleImputer</span><span class="p">(</span><span class="n">strategy</span><span class="o">=</span><span class="s2">"median"</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Imputing the data</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [135]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">imputer</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">dementia</span><span class="p">[</span><span class="n">numerical</span><span class="p">])</span>
    <span class="n">dementia</span><span class="p">[</span><span class="n">numerical</span><span class="p">]</span> <span class="o">=</span> <span class="n">imputer</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">dementia</span><span class="p">[</span><span class="n">numerical</span><span class="p">])</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Checking features that have missing data</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [136]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[136]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>MR Delay    0
    M/F         0
    Age         0
    EDUC        0
    SES         0
    MMSE        0
    eTIV        0
    nWBV        0
    dtype: int64</pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h3 id="Feature-Scaling">Feature Scaling<a class="anchor-link" href="#Feature-Scaling">¶</a></h3>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Extracting features that will be scaled</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [137]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">numerical_scale</span> <span class="o">=</span> <span class="p">[</span><span class="s1">'MR Delay'</span><span class="p">,</span><span class="s1">'Age'</span><span class="p">,</span><span class="s1">'EDUC'</span><span class="p">,</span><span class="s1">'SES'</span><span class="p">,</span><span class="s1">'MMSE'</span><span class="p">,</span><span class="s1">'eTIV'</span><span class="p">,</span><span class="s1">'nWBV'</span><span class="p">]</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Importing library for scaling</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [138]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.preprocessing</span> <span class="kn">import</span> <span class="n">StandardScaler</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Scaling features to a range of -3 to 3 to boost model performance</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [139]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">scaler</span> <span class="o">=</span> <span class="n">StandardScaler</span><span class="p">()</span>
    <span class="n">scaler</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">dementia</span><span class="p">[</span><span class="n">numerical_scale</span><span class="p">])</span>
    <span class="n">dementia</span><span class="p">[</span><span class="n">numerical_scale</span><span class="p">]</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">dementia</span><span class="p">[</span><span class="n">numerical_scale</span><span class="p">])</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [140]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">joblib</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">scaler</span><span class="p">,</span> <span class="s2">"scaler_joblib"</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[140]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>['scaler_joblib']</pre>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [141]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">dementia</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[141]:</div>
    <div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
    <div>
    <style scoped="">
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
    <thead>
    <tr style="text-align: right;">
    <th></th>
    <th>MR Delay</th>
    <th>M/F</th>
    <th>Age</th>
    <th>EDUC</th>
    <th>SES</th>
    <th>MMSE</th>
    <th>eTIV</th>
    <th>nWBV</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <th>243</th>
    <td>1.153824</td>
    <td>1.0</td>
    <td>-0.048614</td>
    <td>1.984618</td>
    <td>-0.537880</td>
    <td>0.722419</td>
    <td>1.757963</td>
    <td>0.221513</td>
    </tr>
    <tr>
    <th>224</th>
    <td>0.104165</td>
    <td>1.0</td>
    <td>1.384521</td>
    <td>-0.861550</td>
    <td>1.322144</td>
    <td>0.722419</td>
    <td>1.430327</td>
    <td>-0.348265</td>
    </tr>
    <tr>
    <th>314</th>
    <td>-0.953327</td>
    <td>0.0</td>
    <td>0.211956</td>
    <td>1.273076</td>
    <td>-1.467892</td>
    <td>0.722419</td>
    <td>-1.357257</td>
    <td>0.465703</td>
    </tr>
    <tr>
    <th>68</th>
    <td>-0.953327</td>
    <td>0.0</td>
    <td>-0.960609</td>
    <td>-0.505779</td>
    <td>1.322144</td>
    <td>0.722419</td>
    <td>-0.734213</td>
    <td>1.578127</td>
    </tr>
    <tr>
    <th>142</th>
    <td>-0.246766</td>
    <td>1.0</td>
    <td>-1.090894</td>
    <td>-0.861550</td>
    <td>1.322144</td>
    <td>0.468340</td>
    <td>-0.309899</td>
    <td>0.194381</td>
    </tr>
    <tr>
    <th>...</th>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    </tr>
    <tr>
    <th>255</th>
    <td>-0.018034</td>
    <td>0.0</td>
    <td>1.514806</td>
    <td>0.561534</td>
    <td>0.392132</td>
    <td>0.722419</td>
    <td>-1.077961</td>
    <td>0.357174</td>
    </tr>
    <tr>
    <th>41</th>
    <td>-0.953327</td>
    <td>0.0</td>
    <td>-2.002889</td>
    <td>0.561534</td>
    <td>0.392132</td>
    <td>0.722419</td>
    <td>-0.981282</td>
    <td>2.012244</td>
    </tr>
    <tr>
    <th>276</th>
    <td>-0.108900</td>
    <td>0.0</td>
    <td>-0.700039</td>
    <td>-1.217321</td>
    <td>1.322144</td>
    <td>0.214261</td>
    <td>-1.137043</td>
    <td>0.275777</td>
    </tr>
    <tr>
    <th>94</th>
    <td>-0.052500</td>
    <td>0.0</td>
    <td>1.123951</td>
    <td>0.205763</td>
    <td>-0.537880</td>
    <td>-1.310215</td>
    <td>-0.068201</td>
    <td>0.465703</td>
    </tr>
    <tr>
    <th>16</th>
    <td>-0.050934</td>
    <td>1.0</td>
    <td>-0.960609</td>
    <td>-0.861550</td>
    <td>-0.537880</td>
    <td>-0.802056</td>
    <td>-0.084314</td>
    <td>1.632392</td>
    </tr>
    </tbody>
    </table>
    <p>268 rows × 8 columns</p>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h2 id="Model-Building">Model Building<a class="anchor-link" href="#Model-Building">¶</a></h2>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [142]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="c1"># renaming data to X_train</span>
    <span class="n">X_train</span> <span class="o">=</span> <span class="n">dementia</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Preprocessing Validation data</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [143]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">X_test</span><span class="p">[</span><span class="n">numerical</span><span class="p">]</span> <span class="o">=</span> <span class="n">imputer</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_test</span><span class="p">[</span><span class="n">numerical</span><span class="p">])</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [144]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">X_test</span><span class="p">[</span><span class="n">numerical_scale</span><span class="p">]</span> <span class="o">=</span> <span class="n">scaler</span><span class="o">.</span><span class="n">transform</span><span class="p">(</span><span class="n">X_test</span><span class="p">[</span><span class="n">numerical_scale</span><span class="p">])</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [145]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">X_test</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[145]:</div>
    <div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
    <div>
    <style scoped="">
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: left;
        }
    </style>
    <table border="1" class="dataframe">
    <thead>
    <tr style="text-align: left;">
    <th></th>
    <th>MR Delay</th>
    <th>M/F</th>
    <th>Age</th>
    <th>EDUC</th>
    <th>SES</th>
    <th>MMSE</th>
    <th>eTIV</th>
    <th>nWBV</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <th>213</th>
    <td>0.538128</td>
    <td>0.0</td>
    <td>-0.309184</td>
    <td>1.273076</td>
    <td>-0.537880</td>
    <td>0.722419</td>
    <td>-0.513999</td>
    <td>0.574233</td>
    </tr>
    <tr>
    <th>28</th>
    <td>0.154298</td>
    <td>1.0</td>
    <td>1.775376</td>
    <td>-2.284634</td>
    <td>1.322144</td>
    <td>-1.056135</td>
    <td>0.925447</td>
    <td>-2.301790</td>
    </tr>
    <tr>
    <th>87</th>
    <td>-0.184099</td>
    <td>0.0</td>
    <td>-0.439469</td>
    <td>-0.861550</td>
    <td>1.322144</td>
    <td>-0.293898</td>
    <td>-0.240075</td>
    <td>0.709894</td>
    </tr>
    <tr>
    <th>328</th>
    <td>0.019566</td>
    <td>1.0</td>
    <td>0.993666</td>
    <td>-0.150008</td>
    <td>-0.537880</td>
    <td>-1.310215</td>
    <td>0.291661</td>
    <td>-1.786276</td>
    </tr>
    <tr>
    <th>222</th>
    <td>-0.224832</td>
    <td>1.0</td>
    <td>-0.700039</td>
    <td>0.561534</td>
    <td>-1.467892</td>
    <td>-2.580611</td>
    <td>0.356114</td>
    <td>-1.243631</td>
    </tr>
    </tbody>
    </table>
    </div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h3 id="Bagging">Bagging<a class="anchor-link" href="#Bagging">¶</a></h3>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Importing library for bagging .i.e Random Forest</p>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [146]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="kn">import</span> <span class="n">RandomForestClassifier</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [147]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">bagger</span> <span class="o">=</span> <span class="n">RandomForestClassifier</span><span class="p">(</span><span class="n">random_state</span><span class="o">=</span><span class="mi">51</span><span class="p">,</span> <span class="n">n_jobs</span><span class="o">=-</span><span class="mi">1</span><span class="p">,</span> <span class="n">n_estimators</span><span class="o">=</span><span class="mi">40</span><span class="p">,</span> <span class="n">max_depth</span><span class="o">=</span><span class="mi">15</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [148]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">bagger</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
    <span class="n">predictions</span> <span class="o">=</span> <span class="n">bagger</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h4 id="Bagging-Performance">Bagging Performance<a class="anchor-link" href="#Bagging-Performance">¶</a></h4>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [149]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.metrics</span> <span class="kn">import</span> <span class="n">accuracy_score</span><span class="p">,</span> <span class="n">confusion_matrix</span><span class="p">,</span> <span class="n">f1_score</span><span class="p">,</span>  <span class="n">recall_score</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [150]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The accuracy is </span><span class="si">{</span><span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The f1 score is </span><span class="si">{</span><span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span> 
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The recall is </span><span class="si">{</span><span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
    <pre>The accuracy is 85.29 %
    The f1 score is 82.14 %
    The recall is 85.19 %
    </pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Confusion Matrix</p>
    <table>
    <thead>
    <tr>
    <th></th>
    <th>0</th>
    <th>1</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>0</td>
    <td>TN</td>
    <td>FP</td>
    </tr>
    <tr>
    <td>1</td>
    <td>FN</td>
    <td>TP</td>
    </tr>
    </tbody>
    </table>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [151]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">confusion_matrix</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">),</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cbar</span><span class="o">=</span><span class="kc">False</span><span class="p">);</span>
    <span class="c1"># TN   FP</span>
    <span class="c1"># FN*   TP - Recall</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
    <img alt="No description has been provided for this image" class="" src="data:image/png;base64,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"/>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h3 id="Stacking">Stacking<a class="anchor-link" href="#Stacking">¶</a></h3>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Algorithms used for stacking</p>
    <ul>
    <li>Decision Tree</li>
    <li>Naive Bayes</li>
    <li>KNN</li>
    </ul>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [152]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.ensemble</span> <span class="kn">import</span> <span class="n">StackingClassifier</span>
    <span class="kn">from</span> <span class="nn">sklearn.tree</span> <span class="kn">import</span> <span class="n">DecisionTreeClassifier</span>
    <span class="kn">from</span> <span class="nn">sklearn.naive_bayes</span> <span class="kn">import</span> <span class="n">GaussianNB</span>
    <span class="kn">from</span> <span class="nn">sklearn.neighbors</span> <span class="kn">import</span> <span class="n">KNeighborsClassifier</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [153]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">estimators</span> <span class="o">=</span> <span class="p">[</span>
        <span class="p">(</span><span class="s1">'dt'</span><span class="p">,</span> <span class="n">DecisionTreeClassifier</span><span class="p">(</span><span class="n">max_depth</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">max_leaf_nodes</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">51</span><span class="p">)),</span>
        <span class="p">(</span><span class="s1">'nb'</span><span class="p">,</span> <span class="n">GaussianNB</span><span class="p">()),</span>
        <span class="p">(</span><span class="s1">'knn'</span><span class="p">,</span> <span class="n">KNeighborsClassifier</span><span class="p">(</span><span class="n">n_neighbors</span><span class="o">=</span><span class="mi">10</span><span class="p">))]</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [154]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">stacker</span> <span class="o">=</span> <span class="n">StackingClassifier</span><span class="p">(</span><span class="n">estimators</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [155]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">stacker</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[155]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>StackingClassifier(estimators=[('dt',
                                    DecisionTreeClassifier(max_depth=4,
                                                        max_leaf_nodes=4,
                                                        random_state=51)),
                                ('nb', GaussianNB()),
                                ('knn', KNeighborsClassifier(n_neighbors=10))])</pre>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [156]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">predictions</span> <span class="o">=</span> <span class="n">stacker</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h4 id="Stacking-Performance">Stacking Performance<a class="anchor-link" href="#Stacking-Performance">¶</a></h4>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [157]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The accuracy is </span><span class="si">{</span><span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The f1 score is </span><span class="si">{</span><span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span> 
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The recall is </span><span class="si">{</span><span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
    <pre>The accuracy is 85.29 %
    The f1 score is 80.77 %
    The recall is 77.78 %
    </pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Confusion Matrix</p>
    <table>
    <thead>
    <tr>
    <th></th>
    <th>0</th>
    <th>1</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>0</td>
    <td>TN</td>
    <td>FP</td>
    </tr>
    <tr>
    <td>1</td>
    <td>FN</td>
    <td>TP</td>
    </tr>
    </tbody>
    </table>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [158]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">confusion_matrix</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">),</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cbar</span><span class="o">=</span><span class="kc">False</span><span class="p">);</span>
    <span class="c1"># TN   FP</span>
    <span class="c1"># FN*   TP - Recall</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
    <img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAW0AAAD3CAYAAADWiwWzAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAJGUlEQVR4nO3cf6zVdR3H8ff9AXr1ooaQiAitTGpuQZjVjEuk3FG6mpYFul3oB0pR6JyU4gRTG4O0XN0QFV06caDNNtkqyqsBi1ISuzpbMxVFRLyFgAIl917utz/aKEou/rp8z9vzePx1z/nefff65z73ud+ze2uKoigCgBRqyx4AwOsn2gCJiDZAIqINkIhoAyRS35c379qyvi9vD29Jw9CmsifAa+ru3LTfa07aAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAiog2QiGgDJCLaAImINkAi9WUP4LXt2bMnrlzwo3j2uU1RV1sb11x+cfz45ttjy9ZtERHxwuaO+NBJH4jrrp5d8lKIGDz46Fj74Ir49BmT44knni57zjuaaFeolWseioiIJTf+INY+8lhc27o4WhdcGRERL7+yI74687K49MLpZU6EiIior6+PRTcsiH+++mrZU6rC63480tPT05c7+B+njzs1vvudiyIiYvOLHXH0wKP2Xlt465I475zPxeBBA0taB//x/QVz4uab74jNL7xY9pSq0Gu0N27cGDNmzIhx48bFhAkTYvz48XHBBRfEM888c7D2VbX6+rq4/JrrYt71i6J5/NiIiHhp2/Z46OH2OOuMCSWvg4gpLV+KLVu2xm/uW1X2lKpRUxRFsb+LU6ZMiUsuuSRGjRq197329vaYP39+LFu27IA379qy/u1ZWeW2vLQ1zj3/4rj3zpti+a/a4uUdO2L61HPLnpVew9Cmsiek99v774miKKIoihg16qR48sn1cdbnvxIdHX8ve1pq3Z2b9nut12fanZ2d+wQ7ImL06NFvyyh6t3zF/dHx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"/>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h3 id="Boosting">Boosting<a class="anchor-link" href="#Boosting">¶</a></h3>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [159]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">xgboost</span> <span class="kn">import</span> <span class="n">XGBClassifier</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [160]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">booster</span> <span class="o">=</span> <span class="n">XGBClassifier</span><span class="p">(</span><span class="n">random_state</span><span class="o">=</span><span class="mi">51</span><span class="p">,</span> <span class="n">n_estimators</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span> <span class="n">max_depth</span><span class="o">=</span><span class="mi">23</span><span class="p">,</span> <span class="n">learning_rate</span><span class="o">=</span><span class="mf">0.5</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [161]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">booster</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[161]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>XGBClassifier(base_score=0.5, booster='gbtree', callbacks=None,
                colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,
                early_stopping_rounds=None, enable_categorical=False,
                eval_metric=None, gamma=0, gpu_id=-1, grow_policy='depthwise',
                importance_type=None, interaction_constraints='',
                learning_rate=0.5, max_bin=256, max_cat_to_onehot=4,
                max_delta_step=0, max_depth=23, max_leaves=0, min_child_weight=1,
                missing=nan, monotone_constraints='()', n_estimators=60, n_jobs=0,
                num_parallel_tree=1, predictor='auto', random_state=51,
                reg_alpha=0, reg_lambda=1, ...)</pre>
    </div>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [162]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">predictions</span> <span class="o">=</span> <span class="n">booster</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">X_test</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h4 id="Boosting-Performance">Boosting Performance<a class="anchor-link" href="#Boosting-Performance">¶</a></h4>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [163]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The accuracy is </span><span class="si">{</span><span class="n">accuracy_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The f1 score is </span><span class="si">{</span><span class="n">f1_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span> 
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"The recall is </span><span class="si">{</span><span class="n">recall_score</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span><span class="w"> </span><span class="n">predictions</span><span class="p">)</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">100</span><span class="si">:</span><span class="s2">.2f</span><span class="si">}</span><span class="s2"> %"</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain" tabindex="0">
    <pre>The accuracy is 86.76 %
    The f1 score is 83.64 %
    The recall is 85.19 %
    </pre>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <p>Confusion Matrix</p>
    <table>
    <thead>
    <tr>
    <th></th>
    <th>0</th>
    <th>1</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>0</td>
    <td>TN</td>
    <td>FP</td>
    </tr>
    <tr>
    <td>1</td>
    <td>FN</td>
    <td>TP</td>
    </tr>
    </tbody>
    </table>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [164]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">confusion_matrix</span><span class="p">(</span><span class="n">y_test</span><span class="p">,</span> <span class="n">predictions</span><span class="p">),</span> <span class="n">annot</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">cbar</span><span class="o">=</span><span class="kc">False</span><span class="p">);</span>
    <span class="c1"># TN   FP</span>
    <span class="c1"># FN*   TP - Recall</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child">
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
    <div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
    <img alt="No description has been provided for this image" class="" src="data:image/png;base64,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"/>
    </div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
    </div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
    <h3 id="Saving-The-Model">Saving The Model<a class="anchor-link" href="#Saving-The-Model">¶</a></h3>
    </div>
    </div>
    </div>
    </div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper" tabindex="0">
    <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
    </div>
    <div class="jp-InputArea jp-Cell-inputArea">
    <div class="jp-InputPrompt jp-InputArea-prompt">In [165]:</div>
    <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
    <div class="cm-editor cm-s-jupyter">
    <div class="highlight hl-ipython3"><pre><span></span><span class="n">joblib</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">booster</span><span class="p">,</span> <span class="s2">"model_joblib"</span><span class="p">)</span>
    </pre></div>
    </div>
    </div>
    </div>
    </div>
    <div class="jp-Cell-outputWrapper">
    <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
    </div>
    <div class="jp-OutputArea jp-Cell-outputArea">
    <div class="jp-OutputArea-child jp-OutputArea-executeResult">
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[165]:</div>
    <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain" tabindex="0">
    <pre>['model_joblib']</pre>
    </div>
    </div>
    </div>
    </div>
    </div>
        """,
        height=9700,width=800
    )

